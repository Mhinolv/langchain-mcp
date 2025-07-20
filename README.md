# LangChain MCP

A Python project that integrates LangChain with Model Context Protocol (MCP) adapters, enabling powerful AI applications with stateful multi-actor capabilities.

## Features

- **LangChain Integration**: Leverages LangChain with OpenAI for LLM functionality
- **MCP Adapters**: Uses LangChain MCP adapters for Model Context Protocol support
- **LangGraph**: Builds stateful, multi-actor applications with graph-based workflows
- **MCP Servers**: Includes example math and weather MCP servers
- **Modern Python**: Built with Python 3.12+ and UV for dependency management

## Quick Start

### Prerequisites

- Python 3.12 or higher
- UV (recommended) or pip for dependency management

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd langchain-mcp

# Install dependencies with UV
uv sync

# Or with pip
pip install -e .
```

### Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Running

```bash
# Run with UV
uv run main.py

# Or with Python
python main.py
```

## Dependencies

- `langchain-mcp-adapters>=0.1.9`: Core MCP adapter functionality
- `langchain[openai]>=0.3.26`: LangChain with OpenAI integration
- `langgraph>=0.5.3`: Graph-based application framework
- `python-dotenv>=1.1.1`: Environment variable management
- `isort>=6.0.1`: Python import sorting utility

## Project Structure

```
langchain-mcp/
├── main.py              # Application entry point
├── pyproject.toml       # Project configuration
├── uv.lock             # UV lock file
├── .env                # Environment variables (create this)
├── CLAUDE.md           # Claude Code project instructions
├── README.md           # This file
└── server/             # MCP server modules
    ├── __init__.py
    ├── math_server.py   # Math operations MCP server
    └── weather_server.py # Weather information MCP server
```

## MCP Servers

The project includes example MCP servers that demonstrate Model Context Protocol functionality:

### Math Server (`server/math_server.py`)
- **Tools**: `add`, `multiply`
- **Transport**: stdio
- **Purpose**: Provides basic mathematical operations

### Weather Server (`server/weather_server.py`)
- **Tools**: `get_weather`
- **Transport**: SSE (Server-Sent Events)
- **Purpose**: Provides weather information for locations

### Running MCP Servers

```bash
# Run math server
python server/math_server.py

# Run weather server
python server/weather_server.py
```