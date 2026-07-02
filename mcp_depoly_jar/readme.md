# MCP Spring Boot Deploy Service

这是一个本地 MCP 服务，用于将 Spring Boot 项目打包成 jar，并将构建产物部署到远程服务器。

## 运行原理与流程

1. 用户通过 MCP 客户端或 Agent 发起部署请求。
2. MCP 客户端将请求发送给本地运行的 `server2.py`。
3. `server2.py` 从 `config.json` 读取配置后，在 `project_dir` 目录执行 Maven 打包。
4. 打包成功后，将生成的 jar 上传到远程 `deploy_path`。
5. 上传完成后，在远程目录执行 `sh start.sh`，完成服务重启。
6. 也可以查询当前配置和远程服务状态，用于审计与故障排查。

## 主要功能

- 使用 Maven 打包 Spring Boot 项目
- 将构建生成的 jar 上传到远程服务器
- 在远程服务器执行重启脚本
- 查看当前部署配置
- 检查远程服务运行状态

## 代码说明

`server2.py` 是当前推荐入口，已添加 Maven 打包与部署一体化流程。
`server.py` 目前与 `server2.py` 功能大部分相同，读者可重点关注 `server2.py`。

## 目录结构

```
mcp_depoly_jar/
├── server.py
├── server2.py
├── config.json
├── requirements.txt
└── readme.md
```

## 环境要求

- Python 3.10+
- 已安装依赖：`mcp`、`paramiko`、`scp`

## 安装依赖

```bash
cd mcp_depoly_jar
pip install -r requirements.txt
```

## 配置说明

### 工具执行流程

1. 读取 `config.json` 中的本地项目目录、Maven 配置和远程服务器信息。
2. 先在本地执行 Maven `clean package`。
3. 打包产物生成后，通过 SCP 上传到远程部署目录。
4. 上传后执行远程 `sh start.sh` 来重启服务。
5. 可以单独检查本地配置或远程服务运行状态。

### 配置示例

下面示例仅用于说明配置格式，避免在 README 中直接暴露真实工程名、jar 名称或敏感信息。

```json
{
  "project_dir": "D:\projects\springboot-app",
  "jar_path": "target\app-service.jar",
  "maven_home": "D:\tools\maven\apache-maven-3.9.7",
  "maven_settings": "D:\config\maven\settings.xml",
  "server": {
    "host": "192.168.1.100",
    "port": 22,
    "username": "deploy",
    "password": "your_password_here"
  },
  "deploy_path": "/opt/app/service"
}
```

### 字段说明

| 字段 | 说明 |
|------|------|
| `project_dir` | Spring Boot 项目根目录，Maven 在此目录执行打包 |
| `jar_path` | 本地 jar 产物路径，支持相对 `project_dir` 或绝对路径 |
| `maven_home` | Maven 安装目录，用于定位 `mvn` 命令 |
| `maven_settings` | Maven settings.xml 路径，用于私服、镜像等配置 |
| `server.host` | 远程服务器地址 |
| `server.port` | SSH 端口，通常为 22 |
| `server.username` | SSH 登录用户名 |
| `server.password` | SSH 登录密码 |
| `deploy_path` | 远程服务器上的部署目录 |

> ⚠️ 为了安全与审计，`config.json` 应该保留在本地，不要提交到 GitHub。README 中仅保留配置示例。

## 启动方式

运行 `server2.py`：

```bash
cd mcp_depoly_jar
python server2.py
```

默认启动为标准输入/输出模式，适合本地 MCP 客户端或 Agent 连接。

### 可选 SSE 模式

如果希望远程连接，可以改成 SSE 模式：

```python
mcp.run(transport="sse", host="0.0.0.0", port=9000)
```

这并不是一个自带网页界面，而是一个支持 MCP SSE 的服务端入口，需要客户端来访问。

## 本地测试

1. 确认 `config.json` 中的 `project_dir`、`jar_path`、`maven_home`、`maven_settings` 以及远程服务器配置正确。
2. 启动服务：

```bash
cd mcp_depoly_jar
python server2.py
```

3. 使用 MCP 客户端或 Agent 发起部署请求：
   - 先执行本地 Maven 打包。
   - 然后执行上传并重启服务。
4. 单独验证 Maven 打包逻辑：

```bash
cd mcp_depoly_jar
python -c "from server2 import load_config, _package_springboot; print(_package_springboot(load_config()))"
```

5. 查看日志文件：
   - `logs/server.log`

## 运行提示

- 运行 `python server2.py` 后，服务将在本地等待 MCP 调用。
- 如果缺少依赖，请先安装：
  ```bash
  pip install mcp paramiko scp
  ```
- 远程部署目录中必须存在 `start.sh`，并确保它可执行。
- 当前没有自动备份旧 jar 的逻辑，必要时请在部署前手动备份或扩展代码。

## Agent 配置示例

### Qoder-CN

```json
{
  "mcpServers": {
    "deploy_service": {
      "command": "python",
      "args": [
        "E:/xxx/server2.py"
      ],
      "env": {
        "NO_PROXY": "*",
        "no_proxy": "*",
        "HTTP_PROXY": "",
        "HTTPS_PROXY": "",
        "ALL_PROXY": ""
      }
    }
  }
}
```

### ClaudeCode

```json
{
  "mcp": {
    "servers": {
      "deploy_service": {
        "command": "python",
        "args": [
          "E:/xxx/server2.py"
        ],
        "env": {
          "NO_PROXY": "*",
          "no_proxy": "*",
          "HTTP_PROXY": "",
          "HTTPS_PROXY": "",
          "ALL_PROXY": ""
        }
      }
    }
  }
}
```


## 说明

`server2.py` 是当前建议使用的入口，`server.py` 作为兼容版本保留。两者执行流程大体相同，建议读者重点查看 `server2.py`。
