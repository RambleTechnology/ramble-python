# server.py
import os
import json
import logging
import asyncio
import subprocess
import paramiko
from scp import SCPClient
from mcp.server.fastmcp import FastMCP

# ============================================================
# 日志配置：输出到 logs/server.log
# ============================================================
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(log_dir, "server.log"), encoding="utf-8"),
    ]
)
logger = logging.getLogger("mcp-deploy-jar")

# ============================================================
# 加载配置文件
# ============================================================
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")


def load_config() -> dict:
    """从 config.json 加载配置"""
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"配置文件不存在: {CONFIG_FILE}")
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_maven_executable(maven_home: str) -> str:
    """解析 Maven 可执行文件路径。"""
    if not maven_home:
        raise ValueError("配置项 maven_home 未设置")

    mvn = os.path.join(maven_home, "bin", "mvn")
    if os.name == "nt":
        if not mvn.lower().endswith(".cmd"):
            mvn = mvn + ".cmd"

    if not os.path.exists(mvn):
        raise FileNotFoundError(f"Maven 可执行文件未找到: {mvn}")

    return mvn


def _package_springboot(config: dict) -> tuple[bool, str]:
    project_dir = config.get("project_dir")
    maven_home = config.get("maven_home")
    maven_settings = config.get("maven_settings")
    jar_path = config.get("jar_path")

    if not project_dir:
        return False, "❌ 未在配置中找到 project_dir，请配置 Spring Boot 项目目录。"
    if not os.path.isdir(project_dir):
        return False, f"❌ Spring Boot 项目目录不存在: {project_dir}"

    pom_path = os.path.join(project_dir, "pom.xml")
    if not os.path.exists(pom_path):
        return False, f"❌ 项目目录中未找到 pom.xml: {pom_path}"

    try:
        mvn_executable = resolve_maven_executable(maven_home)
    except Exception as e:
        return False, f"❌ Maven 可执行文件解析失败: {e}"

    cmd = [mvn_executable, "clean", "package", "-DskipTests"]
    if maven_settings:
        cmd.extend(["-s", maven_settings])

    logger.info(f"开始 Maven 打包: {project_dir}")
    try:
        process = subprocess.run(
            cmd,
            cwd=project_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=1800,
        )
    except subprocess.TimeoutExpired as e:
        return False, f"❌ Maven 打包超时: {e}"
    except Exception as e:
        return False, f"❌ Maven 打包执行失败: {e}"

    stdout_text = process.stdout.strip()
    stderr_text = process.stderr.strip()
    logger.debug(f"Maven stdout:\n{stdout_text}")
    logger.debug(f"Maven stderr:\n{stderr_text}")

    if process.returncode != 0:
        return False, (
            f"❌ Maven 打包失败，退出码 {process.returncode}。\n"
            f"stdout:\n{stdout_text}\n"
            f"stderr:\n{stderr_text}"
        )

    resolved_jar_path = jar_path
    if not os.path.isabs(resolved_jar_path):
        resolved_jar_path = os.path.join(project_dir, resolved_jar_path)

    if not os.path.exists(resolved_jar_path):
        return False, (
            f"❌ 打包完成但未找到 jar 文件: {resolved_jar_path}\n"
            f"请确认 config.json 中 jar_path 是否指向正确的构建产物。"
        )

    return True, (
        f"✅ Maven 打包成功。\n"
        f"项目目录: {project_dir}\n"
        f"Jar 产物: {resolved_jar_path}"
    )


# ============================================================
# 创建 MCP Server 实例
# ============================================================
mcp = FastMCP("deploy-jar-server")


# ============================================================
# 定义 Tool —— 打包 Spring Boot 项目
# ============================================================
@mcp.tool()
async def package_springboot() -> str:
    """
    使用 Maven 打包 Spring Boot 项目。

    读取 config.json 中的 project_dir、maven_home、maven_settings 和 jar_path，
    在项目目录中执行 `mvn clean package -DskipTests`，并校验 jar 文件是否生成。
    """
    logger.info("----- 收到打包请求 -----")

    try:
        config = load_config()
    except FileNotFoundError as e:
        logger.error(f"配置文件加载失败: {e}")
        return f"配置文件加载失败: {str(e)}"
    except json.JSONDecodeError as e:
        logger.error(f"配置文件解析失败: {e}")
        return f"配置文件解析失败: {str(e)}"

    success, message = await asyncio.to_thread(_package_springboot, config)
    logger.info(f"打包结果: {success} / {message}")
    return message


# ============================================================
# 定义 Tool —— 部署 jar 包到服务器
# ============================================================
@mcp.tool()
async def deploy_jar() -> str:
    """
    部署 jar 包到远程服务器。

    将本地 jar 包通过 SCP 拷贝到服务器指定目录，然后执行 sh start.sh 重启服务。
    所有路径和服务器信息从配置文件读取，无需传入参数。

    当用户提到"部署jar"、"发布服务"、"更新服务"、"重启服务"等意图时调用此工具。

    Returns:
        部署结果描述字符串
    """
    logger.info("----- 收到部署请求 -----")

    # 加载配置
    try:
        config = load_config()
    except FileNotFoundError as e:
        logger.error(f"配置文件加载失败: {e}")
        return f"配置文件加载失败: {str(e)}"
    except json.JSONDecodeError as e:
        logger.error(f"配置文件解析失败: {e}")
        return f"配置文件解析失败: {str(e)}"

    success, package_msg = await asyncio.to_thread(_package_springboot, config)
    if not success:
        logger.error(f"打包失败，停止部署: {package_msg}")
        return f"❌ 打包失败，停止部署。\n{package_msg}"

    jar_path = config["jar_path"]
    if not os.path.isabs(jar_path):
        jar_path = os.path.join(config.get("project_dir", ""), jar_path)

    server = config["server"]
    deploy_path = config["deploy_path"]

    host = server["host"]
    port = server["port"]
    username = server["username"]
    password = server["password"]

    logger.info(f"jar_path: {jar_path}")
    logger.info(f"server: {host}:{port} ({username})")
    logger.info(f"deploy_path: {deploy_path}")

    # 检查本地 jar 文件是否存在
    if not os.path.exists(jar_path):
        logger.error(f"jar 文件不存在: {jar_path}")
        return f"本地 jar 文件不存在: {jar_path}"

    # 获取 jar 文件名
    jar_filename = os.path.basename(jar_path)
    remote_jar_path = os.path.join(deploy_path, jar_filename).replace("\\", "/")

    # 通过 paramiko + scp 执行部署（在线程中运行以兼容 async）
    def _deploy():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        result_lines = []

        try:
            # 1. 连接服务器
            logger.info(f"连接服务器 {host}:{port}...")
            ssh.connect(hostname=host, port=port, username=username, password=password, timeout=30)
            result_lines.append(f"✅ SSH 连接成功: {host}:{port}")

            # 2. SCP 上传 jar 文件
            logger.info(f"上传 jar 文件: {jar_path} -> {remote_jar_path}")
            with SCPClient(ssh.get_transport(), progress=_scp_progress) as scp_client:
                scp_client.put(jar_path, remote_jar_path)
            result_lines.append(f"✅ jar 文件上传成功: {jar_filename} -> {remote_jar_path}")

            # 3. 执行 sh start.sh 重启服务
            start_sh_path = os.path.join(deploy_path, "start.sh").replace("\\", "/")
            logger.info(f"执行重启脚本: sh {start_sh_path}")
            stdin, stdout, stderr = ssh.exec_command(f"cd {deploy_path} && sh start.sh", timeout=60)
            exit_status = stdout.channel.recv_exit_status()
            stdout_text = stdout.read().decode("utf-8", errors="replace")
            stderr_text = stderr.read().decode("utf-8", errors="replace")

            logger.info(f"脚本退出状态: {exit_status}")
            logger.info(f"stdout: {stdout_text}")
            logger.info(f"stderr: {stderr_text}")

            if exit_status == 0:
                result_lines.append(f"✅ 服务重启成功 (exit_status=0)")
                if stdout_text.strip():
                    result_lines.append(f"输出: {stdout_text.strip()}")
            else:
                result_lines.append(f"⚠️ 服务重启异常 (exit_status={exit_status})")
                if stderr_text.strip():
                    result_lines.append(f"错误: {stderr_text.strip()}")
                if stdout_text.strip():
                    result_lines.append(f"输出: {stdout_text.strip()}")

        except paramiko.AuthenticationException as e:
            logger.error(f"SSH 认证失败: {e}")
            result_lines.append(f"❌ SSH 认证失败: {str(e)}")
        except paramiko.SSHException as e:
            logger.error(f"SSH 连接异常: {e}")
            result_lines.append(f"❌ SSH 连接异常: {str(e)}")
        except Exception as e:
            logger.error(f"部署异常: {e}", exc_info=True)
            result_lines.append(f"❌ 部署异常: {str(e)}")
        finally:
            ssh.close()
            logger.info("SSH 连接已关闭")

        return "\n".join(result_lines)

    # 在线程池中执行同步的 SSH/SCP 操作
    result = await asyncio.to_thread(_deploy)
    logger.info(f"部署结果: {result}")
    return result


def _scp_progress(filename, size, sent):
    """SCP 传输进度回调"""
    percent = (sent / size) * 100 if size > 0 else 0
    logger.debug(f"传输 {filename}: {sent}/{size} ({percent:.1f}%)")


# ============================================================
# 定义 Tool —— 查看当前配置
# ============================================================
@mcp.tool()
async def show_config() -> str:
    """
    查看当前部署配置信息。

    返回配置文件中的 jar 路径、服务器地址和部署路径（隐藏密码）。
    当用户提到"查看配置"、"当前配置是什么"等意图时调用此工具。

    Returns:
        配置信息描述字符串（密码已隐藏）
    """
    try:
        config = load_config()
    except FileNotFoundError as e:
        return f"配置文件不存在: {str(e)}"
    except json.JSONDecodeError as e:
        return f"配置文件解析失败: {str(e)}"

    server = config["server"]
    masked_password = server["password"][:2] + "****" if len(server["password"]) > 2 else "****"

    info = (
        f"📦 jar 路径: {config['jar_path']}\n"
        f"🖥️ 服务器: {server['host']}:{server['port']} ({server['username']})\n"
        f"🔑 密码: {masked_password}\n"
        f"📁 部署路径: {config['deploy_path']}"
    )
    return info


# ============================================================
# 定义 Tool —— 检查远程服务状态
# ============================================================
@mcp.tool()
async def check_service_status() -> str:
    """
    检查远程服务器上服务的运行状态。

    通过 SSH 连接服务器，检查 jar 进程是否在运行。
    当用户提到"检查服务状态"、"服务是否正常运行"等意图时调用此工具。

    Returns:
        服务状态描述字符串
    """
    try:
        config = load_config()
    except FileNotFoundError as e:
        return f"配置文件不存在: {str(e)}"

    server = config["server"]
    deploy_path = config["deploy_path"]
    jar_filename = os.path.basename(config["jar_path"])

    def _check():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(
                hostname=server["host"],
                port=server["port"],
                username=server["username"],
                password=server["password"],
                timeout=10
            )
            # 检查 jar 进程是否运行
            stdin, stdout, stderr = ssh.exec_command(f"ps -ef | grep {jar_filename} | grep -v grep")
            ps_output = stdout.read().decode("utf-8", errors="replace").strip()

            if ps_output:
                return f"✅ 服务正在运行\n进程信息:\n{ps_output}"
            else:
                return f"⚠️ 服务未运行 (未找到 {jar_filename} 进程)"
        except Exception as e:
            return f"❌ 检查失败: {str(e)}"
        finally:
            ssh.close()

    return await asyncio.to_thread(_check)


# ============================================================
# 启动入口
# ============================================================
if __name__ == "__main__":
    logger.info("========== MCP Deploy Jar Server 启动 ==========")
    logger.info(f"日志文件: {os.path.join(log_dir, 'server.log')}")
    logger.info(f"配置文件: {CONFIG_FILE}")

    # 方式一: stdio 模式 (本地使用，配合 Claude Desktop / Qoder 等)
    mcp.run(transport="stdio")

    # 方式二: SSE 模式 (远程部署，供多个客户端连接)
    # mcp.run(transport="sse", host="0.0.0.0", port=9000)
