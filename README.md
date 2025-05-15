
这是一个只有  **9行** 代码的并且可运行的，mcp（model context protocol）server的demo。适合想要上手学习mcp的新手。

## 第一步 下载代码
下载完整代码或者直接复制下面9行代码。
```python
import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="time-service")

@mcp.tool(name="get_current_time", description="获取当前系统时间")
def get_current_time(format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    now = datetime.datetime.now()
    return now.strftime(format_str)
if __name__ == "__main__":
    mcp.run(transport='sse')  # 使用SSE模式运行服务
```

## 第二步 配置conda环境
 conda.exe create -n mcp python=3.12
 conda activate mcp

## 第三步 安装依赖包
pip install "mcp[cli]"
pip install psutil

## 第四步 运行代码
python mcp_get_current_time.py

## 第五步 在聊天机器人中配置mcp server并使用


