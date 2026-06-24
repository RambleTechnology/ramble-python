# MCP Deploy Jar Service

基于 FastMCP 的 MCP 服务，用于将本地构建好的 jar 包部署到远程服务器指定目录，并执行 `sh start.sh` 重启服务。

## 功能

- 通过 SCP 将 jar 包上传到远程服务器
- 在远程服务器执行 `sh start.sh` 重启服务
- 查看当前部署配置
- 检查远程服务运行状态

## 目录结构

```
mcp_depoly_jar/
├── server.py           # MCP 服务主程序
├── config.json         # 配置文件（敏感信息，已加入 .gitignore）
├── requirements.txt    # Python 依赖
└── readme.md           # 本文件
```

## 环境要求

- Python 3.10+
- 已安装依赖：`mcp`、`paramiko`、`scp`

## 安装依赖

```bash
cd mcp_depoly_jar
pip install -r requirements.txt
```

## 配置文件

首次使用前，编辑 `config.json` 文件，填写正确的服务器信息和部署路径。

```json
{
  "jar_path": "D:\\xxx\\xxx\\target\\xxx.jar",
  "server": {
    "host": "192.168.x.x",
    "port": 22,
    "username": "root",
    "password": "your_password_here"
  },
  "deploy_path": "/opt/xxx/xxx"
}
```

| 字段 | 说明 |
|------|------|
| `jar_path` | 本地 jar 包路径 |
| `server.host` | 远程服务器 IP |
| `server.port` | SSH 端口，默认 22 |
| `server.username` | SSH 用户名 |
| `server.password` | SSH 密码 |
| `deploy_path` | 服务器上的部署目录 |

> ⚠️ `config.json` 已加入 `.gitignore`，不会被提交到 GitHub，请勿手动将其加入版本控制。

## 启动服务

```bash
cd mcp_depoly_jar
python server.py
```

默认以 `stdio` 模式启动，可与 Claude Desktop、Qoder 等支持 MCP 的客户端配合使用。

## MCP Tools

| 工具名 | 说明 |
|--------|------|
| `deploy_jar` | 将 jar 包部署到远程服务器并执行 `sh start.sh` 重启服务 |
| `show_config` | 查看当前配置（密码会脱敏显示） |
| `check_service_status` | 检查远程服务器上 jar 进程是否运行 |

## 使用示例

在支持 MCP 的客户端中，直接调用工具即可：

- "帮我部署 jar 包" → 调用 `deploy_jar`
- "查看当前部署配置" → 调用 `show_config`
- "检查服务运行状态" → 调用 `check_service_status`

## 日志

运行日志输出到 `mcp_depoly_jar/logs/server.log`，可用于排查部署问题。

## 注意事项

1. 请确保远程服务器已开启 SSH 服务，且端口、账号、密码正确。
2. 部署目录下需存在 `start.sh` 脚本，并具有可执行权限。
3. 如需支持 SSH 密钥认证，可后续扩展 `server.py` 中的认证逻辑。
4. 当前默认不备份旧 jar 包，如需备份请在部署前手动处理或在 `server.py` 中添加相关逻辑。
