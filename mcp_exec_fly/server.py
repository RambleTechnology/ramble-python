# server.py
import sys
import os
import logging
import httpx
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
logger = logging.getLogger("mcp-server")

# ============================================================
# 创建 MCP Server 实例
# ============================================================
mcp = FastMCP("fly-inspection-server")

# Spring Boot 服务地址，按需修改
BASE_URL = "http://192.168.1.230:8385/aircraft/qingpuga/fly/takeOff"


# ============================================================
# 定义 Tool —— 大模型会看到这个描述并决定何时调用
# ============================================================
@mcp.tool()
async def execute_inspection_task(job_id: str) -> str:
    """
    执行飞行巡查任务。

    当用户提到"执行巡查任务"、"起飞"、"飞行任务"等意图时调用此工具。
    从用户的自然语言中提取数字作为 job_id。
    例如：
      - "执行12345巡查任务" → job_id="12345"
      - "起飞任务 67890"   → job_id="67890"
      - "开始巡查 ABC-001" → job_id="ABC-001"

    Args:
        job_id: 任务编号，将作为路径参数传递给飞行调度系统
    """

    logger.info("----- 收到工具调用 -----")
    logger.info(f"job_id = {job_id}")

    url = f"{BASE_URL}/{job_id}"
    logger.info(f"请求 URL: {url}")

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.get(url)
            logger.info(f"响应状态码: {response.status_code}")
            logger.info(f"响应内容: {response.text}")

            # 直接返回 Spring Boot 的原始响应，不做成功失败判断
            logger.info(f"返回给客户端: {response.text}")
            return response.text

        except httpx.ConnectError as e:
            logger.error(f"连接失败: {e}")
            return f"无法连接到飞行调度系统 ({BASE_URL})，请确认服务是否启动。"
        except httpx.TimeoutException as e:
            logger.error(f"请求超时: {e}")
            return f"请求超时，飞行调度系统未在 30 秒内响应。"
        except Exception as e:
            logger.error(f"异常: {e}", exc_info=True)
            return f"任务下发异常: {str(e)}"


# ============================================================
# 启动入口
# ============================================================
if __name__ == "__main__":
    logger.info("========== MCP Server 启动 ==========")
    logger.info(f"日志文件: {os.path.join(log_dir, 'server.log')}")
    logger.info(f"Spring Boot 地址: {BASE_URL}")

    # 方式一: stdio 模式 (本地使用，配合 Claude Desktop 等)
    mcp.run(transport="stdio")

    # 方式二: SSE 模式 (远程部署，供多个客户端连接)
    # mcp.run(transport="sse", host="0.0.0.0", port=9000)