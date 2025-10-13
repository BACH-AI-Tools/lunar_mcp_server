# 🚀 快速启动指南 - UVX 一键启动

## 什么是 UVX？

UVX 是 Python 包管理器 UV 提供的命令行工具运行器，类似于 Node.js 的 NPX。它可以直接从 PyPI 下载并运行 Python 包，无需手动安装。

## ⚡ 一键启动

```bash
uvx bach-lunar-mcp
```

就这么简单！无需克隆仓库、创建虚拟环境或安装依赖。

## 📦 在 MCP 客户端中配置

### Cursor IDE 配置

编辑 Cursor 的 MCP 配置文件（通常在 `~/.cursor/mcp.json` 或通过 Cursor 设置）：

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

### Cherry Studio 配置

在 Cherry Studio 的设置中添加 MCP 服务器：

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

### Claude Desktop 配置

编辑 Claude Desktop 配置文件：

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

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

## 🎋 功能列表

### 1. 八字计算 (bazi_calculate)

计算生辰八字，用于命理分析

**示例**：

```
请帮我计算 1990年1月1日 早上8:30 的八字
```

### 2. 历法转换 (calendar_convert)

公历与农历互相转换

**示例**：

```
2024年1月1日 是农历几月几号？
农历2024年正月初一 是公历几月几号？
```

### 3. 黄历查询 (huangli_query)

查询指定日期的黄历信息，包括宜忌、节气、节日等

**示例**：

```
查询 2024年10月1日 的黄历
今天的黄历如何？
```

### 4. 每日运势 (fortune_daily)

获取每日运势和建议

**示例**：

```
今天的运势如何？
2024年10月13日 的运势分析
```

### 5. 节气查询 (jieqi_query)

查询指定年份的二十四节气

**示例**：

```
2024年的二十四节气有哪些？
```

### 6. 五行分析 (wuxing_analyze)

根据生辰信息分析五行强弱

**示例**：

```
分析 1990年1月1日 早上8:30 的五行
```

## 🌟 使用示例

启动 Cursor 或其他 MCP 客户端后，你可以直接对 AI 说：

- "今天的黄历宜忌是什么？"
- "帮我算一下明天适合做什么事情"
- "2024 年春节是公历几月几号？"
- "帮我计算一下我的八字"
- "今年的立春是什么时候？"

AI 会自动调用相应的农历工具来回答你的问题。

## 📚 更多信息

- **PyPI 包地址**: https://pypi.org/project/bach-lunar-mcp/
- **GitHub 仓库**: https://github.com/BACH-AI-Tools/lunar_mcp_server
- **问题反馈**: https://github.com/BACH-AI-Tools/lunar_mcp_server/issues

## 💡 提示

- 首次运行时，UVX 会自动下载并缓存包，可能需要几秒钟
- 后续运行会直接使用缓存，启动速度很快
- 如需更新到最新版本，运行 `uvx --refresh bach-lunar-mcp`

## 🛠️ 系统要求

- Python 3.12+
- UV 包管理器（会自动安装 UVX）

安装 UV：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

**注意**：此工具仅供娱乐和文化研究使用，请理性对待传统历法文化。
