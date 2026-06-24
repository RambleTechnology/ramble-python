import asyncio
import logging
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("test-client")


async def main():
    logger.info("客户端启动，准备连接 MCP Server...")

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        logger.info("MCP Server 连接成功")

        async with ClientSession(read, write) as session:
            await session.initialize()
            logger.info("会话初始化完成")

            # 1. 列出所有工具
            tools = await session.list_tools()
            print("=== 可用工具 ===")
            for t in tools.tools:
                print(f"  {t.name}: {t.description[:60]}...")

            # 2. 调用工具
            print("\n=== 调用 execute_inspection_task ===")
            logger.info("开始调用 execute_inspection_task, job_id=12345")
            result = await session.call_tool(
                "execute_inspection_task",
                arguments={"job_id": "12345"}
            )
            logger.info(f"调用完成，结果: {result.content[0].text}")
            print(f"结果: {result.content[0].text}")


asyncio.run(main())