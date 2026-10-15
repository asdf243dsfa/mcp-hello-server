# mcp-hello-server · 我的第一个 MCP 服务器

最小可运行的 MCP (Model Context Protocol) 服务器示例,Python + FastMCP。

## 工具
- `hello(name)` — 打招呼,返回问候语
- `add(a, b)` — 两数相加

## 使用
```bash
pip install "mcp<2"
```
在 AI 客户端的 MCP 设置里新增服务器:
- command: `python`
- args: 本文件 `server.py` 的完整路径

在客户端里说"用 hello 工具跟我打个招呼"即可验证。

## License
MIT
