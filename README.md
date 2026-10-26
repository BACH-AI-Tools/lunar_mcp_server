# Lunar Calendar MCP Server

[![GitHub Repository](https://img.shields.io/badge/GitHub-BACH--AI--Tools/lunar__mcp__server-blue?style=flat&logo=github)](https://github.com/BACH-AI-Tools/lunar_mcp_server)
[![PyPI version](https://img.shields.io/pypi/v/bach-lunar-mcp.svg)](https://pypi.org/project/bach-lunar-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![MCP Server](https://img.shields.io/badge/MCP-Server-green.svg)](https://modelcontextprotocol.io/)

[中文](README.cn.md) | **English**

A Model Context Protocol (MCP) server for Chinese traditional calendar functions, built with Python 3.12 and lunar-python.

## 🚀 Quick Start (Recommended)

### One-Command Launch with UVX

```bash
uvx bach-lunar-mcp
```

**That's it!** No installation, no virtual environment setup, no dependencies to manage. UVX will automatically download and run the server.

### Configure in Your MCP Client

#### Cursor IDE

```json
{
  "mcpServers": {
    "lunar-calendar": {
      "command": "uvx",
      "args": ["bach-lunar-mcp"]
    }
  }
}
```

#### Claude Desktop

```json
{
  "mcpServers": {
    "lunar-calendar": {
      "command": "uvx",
      "args": ["bach-lunar-mcp"]
    }
  }
}
```

#### Cherry Studio

```json
{
  "mcpServers": {
    "lunar-calendar": {
      "command": "uvx",
      "args": ["bach-lunar-mcp"]
    }
  }
}
```

**📦 PyPI Package**: https://pypi.org/project/bach-lunar-mcp/  
**📖 Quick Start Guide**: [QUICKSTART_UVX.md](QUICKSTART_UVX.md)

---

## Features

🎋 **BaZi Calculation** - Calculate eight characters for fortune telling  
📅 **Calendar Conversion** - Convert between solar and lunar calendars  
🌙 **Huangli Query** - Chinese almanac with daily recommendations  
🔮 **Daily Fortune** - Daily fortune and recommendations  
⭐ **Solar Terms** - Look up solar terms for a given year  
🧮 **Wu Xing Analysis** - Five elements analysis from birth info

## Installation

### Prerequisites

- Python 3.12+
- uv package manager

### Setup

1. **Clone the repository:**

```bash
git clone https://github.com/BACH-AI-Tools/lunar_mcp_server.git
cd lunar_mcp_server
```

2. **Install uv (if not already installed):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **Install project with dependencies:**

```bash
uv sync
```

This will automatically:

- Create a virtual environment with Python 3.12
- Install all dependencies from pyproject.toml
- Generate uv.lock for reproducible builds

## Usage

### As MCP Server

Configure in your MCP client (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "lunar-calendar": {
      "command": "uv",
      "args": ["run", "bach-lunar-mcp"],
      "cwd": "/path/to/lunar_mcp_server"
    }
  }
}
```

### Direct Usage

You can also use the helper functions directly:

```bash
# Run with uv
uv run python -c "
from src.utils import LunarHelper
result = LunarHelper.solar_to_lunar(2024, 1, 1)
print(result['lunar_date_chinese'])  # 二〇二三年冬月二十
"

# Calculate BaZi
uv run python -c "
from src.utils import LunarHelper
result = LunarHelper.get_bazi(1990, 1, 1, 8, 30)
print(result['bazi_string'])  # 己巳 丙子 丙寅 壬辰
"
```

## Available Tools

### 1. bazi_calculate

Calculate BaZi (Eight Characters) for fortune telling.

**Parameters:**

- `birth_date`: Birth date in YYYY-MM-DD format
- `birth_time`: Birth time in HH:MM format

**Example:**

```json
{
  "birth_date": "1990-01-01",
  "birth_time": "08:30"
}
```

### 2. calendar_convert

Convert between solar and lunar calendars.

**Parameters:**

- `date`: Date in YYYY-MM-DD format
- `convert_to`: "lunar" or "solar"
- `is_leap`: Is leap month (optional)

**Example:**

```json
{
  "date": "2024-01-01",
  "convert_to": "lunar"
}
```

### 3. huangli_query

Query Chinese almanac information for a specific date.

**Parameters:**

- `date`: Date in YYYY-MM-DD format

**Example:**

```json
{
  "date": "2024-01-01"
}
```

### 4. fortune_daily

Get daily fortune and recommendations.

**Parameters:**

- `date`: Date in YYYY-MM-DD format

**Example:**

```json
{
  "date": "2024-01-01"
}
```

### 5. jieqi_query

Look up solar terms for a given year.

**Parameters:**

- `year`: Year to query

**Example:**

```json
{
  "year": 2024
}
```

> ⚠️ **Known limitation:** the current implementation only checks the first day of each month, so most queries return few or no solar terms (it does not list all 24). See [issue #3](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/3).

### 6. wuxing_analyze

Analyze Wu Xing (Five Elements) from birth information.

**Parameters:**

- `birth_date`: Birth date in YYYY-MM-DD format
- `birth_time`: Birth time in HH:MM format

**Example:**

```json
{
  "birth_date": "1990-01-01",
  "birth_time": "08:30"
}
```

## Development

### Run the Server Locally

```bash
# Run the MCP server (after `uv sync`)
uv run bach-lunar-mcp
```

### Verify the Installation

```bash
# Check that the helper module imports correctly
uv run python -c "from src.utils import LunarHelper; print('✅ Import works!')"
```

### Install Development Dependencies (optional)

```bash
# Install the `dev` dependency group (pytest, black, isort, mypy)
uv sync --extra dev
```

### Code Formatting

```bash
# Format code
black src/
isort src/

# Type checking
mypy src/
```

## Dependencies

- **mcp**: Model Context Protocol implementation
- **lunar-python**: Chinese lunar calendar library
- **pydantic**: Data validation and settings management

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [lunar-python](https://github.com/6tail/lunar-python) - Excellent Chinese lunar calendar library
- [MCP](https://modelcontextprotocol.io/) - Model Context Protocol specification

---

**Note:** This is a traditional calendar tool for educational and entertainment purposes. Please use responsibly.
