# MCP 飞行巡查服务

基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io) 的飞行巡查任务调度服务，通过自然语言指令触发飞行任务。

---

## 目录

- [项目简介](#项目简介)
- [FastMCP 简介](#fastmcp-简介)
- [项目结构](#项目结构)
- [环境依赖](#环境依赖)
- [使用方法](#使用方法)
  - [启动 MCP Server](#启动-mcp-server)
  - [运行测试客户端](#运行测试客户端)
- [test_client.py 工作原理](#test_clientpy-工作原理)
- [在 Qoder 中配置该 MCP](#在-qoder-中配置该-mcp)
- [日志](#日志)

---

## 项目简介

本项目是一个 MCP Server，对外暴露一个 `execute_inspection_task` 工具（Tool）。当 AI 客户端（如 Claude Desktop、Qoder 等）连接到此 Server 后，用户可以通过自然语言（如"执行12345巡查任务"）触发飞行巡查指令，Server 会将任务 ID 转发到后端 Spring Boot 调度系统完成起飞操作。

---

## FastMCP 简介

[FastMCP](https://github.com/modelcontextprotocol/python-sdk) 是 MCP 官方 Python SDK 内置的高性能框架（FastMCP 1.0 由 PrefectHQ 开发，于 2024 年合并进官方 SDK），用于快速构建 MCP Server 和 Client。

**核心工作方式：**

```
客户端 (Claude / Qoder / test_client.py)
        │
        │  stdio / SSE
        ▼
   FastMCP Server
        │
        │  @mcp.tool() 装饰器注册工具
        ▼
   业务逻辑（HTTP 调用后端服务）
```

- **声明式注册**：通过 `@mcp.tool()` 装饰器将 Python 函数注册为 MCP 工具，函数的 docstring 自动作为工具描述供 AI 模型读取。
- **传输方式**：支持 `stdio`（本地进程通信）和 `sse`（Server-Sent Events，远程 HTTP）两种模式。
- **类型安全**：基于 Pydantic 自动解析参数类型，AI 模型可按 schema 传参。

开源地址：
- 官方 SDK（含 FastMCP）：<https://github.com/modelcontextprotocol/python-sdk>
- FastMCP 独立仓库：<https://github.com/PrefectHQ/fastmcp>
- 文档：<https://gofastmcp.com>

---

## 项目结构

```
mcp_exec_fly/
├── server.py           # MCP Server 主程序
├── test_client.py      # 测试客户端（本地验证 Server 工具）
├── requirements.txt    # Python 依赖
├── .gitignore
└── logs/
    └── server.log      # 运行日志
```

---

## 环境依赖

```bash
pip install -r requirements.txt
```

主要依赖：

| 包名 | 说明 |
|------|------|
| `mcp` | MCP 官方 Python SDK（含 FastMCP） |
| `httpx` | 异步 HTTP 客户端，用于调用后端 Spring Boot 接口 |

---

## 使用方法

### 启动 MCP Server

```bash
python server.py
```

默认以 **stdio** 模式运行（供本地客户端连接）。如需远程访问，修改 `server.py` 末尾为 SSE 模式：

```python
mcp.run(transport="sse", host="0.0.0.0", port=9000)
```

### 运行测试客户端

```bash
python test_client.py
```

该脚本会自动启动 Server 子进程、连接、列出工具并调用 `execute_inspection_task`，详见下文。

---

## test_client.py 工作原理

`test_client.py` 是一个完整的 MCP Client 实现，用于在本地验证 Server 是否正常工作。其工作流程如下：

```
test_client.py
     │
     │ 1. StdioServerParameters(command="python", args=["server.py"])
     │    → 将 server.py 作为子进程启动
     ▼
     │ 2. stdio_client(server_params)
     │    → 通过标准输入/输出（stdin/stdout）建立双向通信管道
     ▼
     │ 3. ClientSession(read, write)
     │    → 创建 MCP 会话，封装 JSON-RPC 协议
     ▼
     │ 4. session.initialize()
     │    → 握手，协商协议版本与能力
     ▼
     │ 5. session.list_tools()
     │    → 获取 Server 注册的所有工具列表及描述
     ▼
     │ 6. session.call_tool("execute_inspection_task", {"job_id": "12345"})
     │    → 调用指定工具，等待并打印返回结果
```

**核心原理：**
- MCP 使用 **JSON-RPC 2.0** 协议，stdio 模式下通过进程的 stdin/stdout 传输消息。
- Client 先启动 Server 子进程，再通过管道完成握手、工具发现和工具调用。
- 这是本地调试 MCP Server 最直接的方式，无需额外网络配置。

---

## 在 Qoder 中配置该 MCP

### 第一步：确认 Server 文件路径

假设项目位于：
```
E:\xxx\server.py
```

### 第二步：打开 Qoder MCP 配置

在 Qoder 中，打开设置（`Ctrl + ,`），搜索 **MCP** 或直接编辑 MCP 配置文件（`mcp.json` / `settings.json` 中的 `mcp.servers` 字段）。

### 第三步：添加 Server 配置

在 MCP servers 配置中加入如下内容：

```json
{
  "mcp": {
    "servers": {
      "fly-inspection": {
        "command": "python",
        "args": ["E:/xxx/server.py"],
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

若机器安装了多个版本的python，command需指定python.exe安装位置。


> **说明**：`command` + `args` 指定如何启动 Server 进程，Qoder 会自动以 stdio 模式与之通信。

### 第四步：重启 Qoder

保存配置后重启 Qoder，等待 MCP Server 连接成功（状态栏或日志中可见 `fly-inspection-server` 已注册）。

### 第五步：使用自然语言调用

在 Qoder 对话框中直接输入自然语言指令：

| 指令示例 | 效果 |
|----------|------|
| `执行12345巡查任务` | 调用 `execute_inspection_task(job_id="12345")` |
| `起飞任务 67890` | 调用 `execute_inspection_task(job_id="67890")` |
| `开始巡查 ABC-001` | 调用 `execute_inspection_task(job_id="ABC-001")` |

Qoder 的大模型会读取工具描述，自动识别意图并从自然语言中提取 `job_id` 参数完成调用。

---

## 日志

Server 运行日志保存在 `logs/server.log`，包含：
- 每次工具调用的 `job_id`
- 发往后端 Spring Boot 的请求 URL 与响应
- 连接失败、超时等异常信息

排查问题时优先查看该文件。
