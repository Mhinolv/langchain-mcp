import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters, stdio_server
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command = "python",
    args = ["/Users/MarkHinojosa/mcp_servers/langchain-mcp/server/weather_server.py"],
)

async def main():
    print("Hello from langchain-mcp!")

if __name__ == "__main__":
    asyncio.run(main())