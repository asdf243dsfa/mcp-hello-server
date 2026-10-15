"""
我亲手搭的第一个 MCP 服务器
运行: pip install "mcp<2"  然后  python server.py
这个文件会被你的 AI 客户端(Qwen 等)直接启动,不用你手动跑。
"""
from mcp.server.fastmcp import FastMCP

# 给你的服务器起个名字
mcp = FastMCP("我的第一个MCP")


@mcp.tool()
def hello(name: str) -> str:
    """跟用户打招呼,参数 name 是对方的名字"""
    return f"你好,{name}!我是你亲手搭的第一个 MCP 工具,调用成功!"


@mcp.tool()
def add(a: float, b: float) -> float:
    """两个数相加,参数 a 和 b 是要加的数字"""
    return a + b


if __name__ == "__main__":
    mcp.run()
