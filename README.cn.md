# 农历 MCP 服务器

[![GitHub Repository](https://img.shields.io/badge/GitHub-BACH--AI--Tools/lunar__mcp__server-blue?style=flat&logo=github)](https://github.com/BACH-AI-Tools/lunar_mcp_server)
[![PyPI version](https://img.shields.io/pypi/v/bach-lunar-mcp.svg)](https://pypi.org/project/bach-lunar-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![MCP Server](https://img.shields.io/badge/MCP-Server-green.svg)](https://modelcontextprotocol.io/)

**中文** | [English](README.md)

基于 Python 3.12 和 lunar-python 构建的中国传统历法模型上下文协议(MCP)服务器。

## 🚀 快速启动（推荐）

### 使用 UVX 一键启动

```bash
uvx bach-lunar-mcp
```

**就这么简单！** 无需安装、无需配置虚拟环境、无需管理依赖。UVX 会自动下载并运行服务器。

### 在 MCP 客户端中配置

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

**📦 PyPI 包地址**: https://pypi.org/project/bach-lunar-mcp/  
**📖 快速启动指南**: [QUICKSTART_UVX.md](QUICKSTART_UVX.md)

---

## 功能特性

🎋 **生辰八字计算** - 计算八字用于命理分析  
📅 **历法转换** - 公历农历互相转换  
🌙 **黄历查询** - 中国传统黄历，包含每日宜忌建议  
🔮 **每日运势** - 基于传统历法的每日运势分析  
⭐ **节气查询** - 查询指定年份的节气  
🧮 **五行分析** - 根据出生信息分析五行属性

## 安装

### 前置要求

- Python 3.12+
- uv 包管理器

### 设置

1. **克隆仓库：**

```bash
git clone https://github.com/BACH-AI-Tools/lunar_mcp_server.git
cd lunar_mcp_server
```

2. **安装 uv（如果尚未安装）：**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **安装项目及依赖：**

```bash
uv sync
```

这将自动：

- 创建 Python 3.12 虚拟环境
- 从 pyproject.toml 安装所有依赖
- 生成 uv.lock 确保构建可重现

## 使用方法

### 作为 MCP 服务器

在 MCP 客户端中配置（例如 Claude Desktop）：

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

### 直接使用

你也可以直接使用辅助函数：

```bash
# 使用uv运行
uv run python -c "
from src.utils import LunarHelper
result = LunarHelper.solar_to_lunar(2024, 1, 1)
print(result['lunar_date_chinese'])  # 二〇二三年冬月二十
"

# 计算八字
uv run python -c "
from src.utils import LunarHelper
result = LunarHelper.get_bazi(1990, 1, 1, 8, 30)
print(result['bazi_string'])  # 己巳 丙子 丙寅 壬辰
"
```

## 可用工具

### 1. bazi_calculate（生辰八字计算）

计算用于命理分析的生辰八字。

**参数：**

- `birth_date`: 出生日期，格式 YYYY-MM-DD
- `birth_time`: 出生时间，格式 HH:MM

**示例：**

```json
{
  "birth_date": "1990-01-01",
  "birth_time": "08:30"
}
```

### 2. calendar_convert（历法转换）

公历和农历之间的相互转换。

**参数：**

- `date`: 日期，格式 YYYY-MM-DD
- `convert_to`: "lunar"（农历）或"solar"（公历）
- `is_leap`: 是否闰月（可选）

**示例：**

```json
{
  "date": "2024-01-01",
  "convert_to": "lunar"
}
```

### 3. huangli_query（黄历查询）

查询指定日期的中国传统黄历信息。

**参数：**

- `date`: 日期，格式 YYYY-MM-DD

**示例：**

```json
{
  "date": "2024-01-01"
}
```

### 4. fortune_daily（每日运势）

获取每日运势和建议。

**参数：**

- `date`: 日期，格式 YYYY-MM-DD

**示例：**

```json
{
  "date": "2024-01-01"
}
```

### 5. jieqi_query（节气查询）

查询指定年份的节气。

**参数：**

- `year`: 查询的年份

**示例：**

```json
{
  "year": 2024
}
```

> ⚠️ **已知限制：** 当前实现只检查每月第一天，因此多数查询返回很少或没有节气（不会列出全部 24 个）。详见 [issue #3](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/3)。

### 6. wuxing_analyze（五行分析）

根据出生信息分析五行属性。

**参数：**

- `birth_date`: 出生日期，格式 YYYY-MM-DD
- `birth_time`: 出生时间，格式 HH:MM

**示例：**

```json
{
  "birth_date": "1990-01-01",
  "birth_time": "08:30"
}
```

## 开发

### 本地运行服务器

```bash
# 运行 MCP 服务器（先执行 `uv sync`）
uv run bach-lunar-mcp
```

### 验证安装

```bash
# 检查辅助模块能否正常导入
uv run python -c "from src.utils import LunarHelper; print('✅ 导入成功!')"
```

### 安装开发依赖（可选）

```bash
# 安装 `dev` 依赖组（pytest、black、isort、mypy）
uv sync --extra dev
```

### 代码格式化

```bash
# 格式化代码
black src/
isort src/

# 类型检查
mypy src/
```

## 依赖

- **mcp**: 模型上下文协议实现
- **lunar-python**: 中国农历库
- **pydantic**: 数据验证和设置管理

## 贡献

1. Fork 仓库
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见[LICENSE](LICENSE)文件。

## 致谢

- [lunar-python](https://github.com/6tail/lunar-python) - 优秀的中国农历库
- [MCP](https://modelcontextprotocol.io/) - 模型上下文协议规范

---

**注意：** 这是一个用于教育和娱乐目的的传统历法工具，请负责任地使用。
