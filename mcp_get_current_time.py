import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="time-service")

@mcp.tool(name="get_current_time", description="获取当前系统时间")
def get_current_time(format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    now = datetime.datetime.now()
    return now.strftime(format_str)
if __name__ == "__main__":
    mcp.run(transport='sse')  # 使用SSE模式运行服务