# Changelog

本文件记录 `bach-lunar-mcp`（GitHub 仓库 `BACH-AI-Tools/lunar_mcp_server`）自 1.0.0 发布以来的变更。

## [Unreleased] — 将随 1.0.1 发布

### 修复（已合并进 main）

- **节气查询返回不完整**（Issue #3）：`jieqi_query` 现返回指定公历年的完整 24 个节气及真实日期（PR #17）
- **五行标签错误**（Issue #4）：黄历与运势显示真实五行与方位，移除占位文案（PR #18）
- **闰月显示负数**（Issue #6）：公历转农历时闰月不再显示为负数月份（PR #19）
- **锁文件不同步**（Issue #5）：锁定 `mcp<2.0` 并重新生成 `uv.lock`，修复 1.0.0 安装即崩问题（PR #21）
- **发布流程**：新增通过 GitHub Releases 触发 PyPI 发布的自动化流程（PR #25）

### 文档整改

- **README.md / README.cn.md（中英双版）**：
  - 修正克隆命令为真实地址 `https://github.com/BACH-AI-Tools/lunar_mcp_server`，并更正目录名为 `lunar_mcp_server`
  - 启动命令由 `python -m src.server` 改为官方入口 `uvx bach-lunar-mcp`
  - 删除不存在的 `quick_test.py` / `run_server.py` 运行示例
  - 开发依赖命令由 `uv add --dev …` 更正为 `uv sync --extra dev`
  - 直接使用示例的导入统一为 `from utils import LunarHelper`
  - 节气功能说明按代码现状更新：`jieqi_query` 现返回指定公历年的完整 24 个节气及真实日期，移除「仅检查每月 1 日」的过时限制说明
  - 每日运势（`fortune_daily`）增加披露：综合指数固定为 ⭐⭐⭐⭐，事业/感情/财运按黄历宜忌关键词匹配，非真实算法，仅供娱乐
  - 开发章节补充测试命令 `uv run pytest`（测试位于 `tests/` 目录）
  - 补全示例输出（如 2024-01-01 → 二〇二三年冬月二十）
- **QUICKSTART_UVX.md**：
  - 节气功能说明按代码现状更新（同 README）
  - 每日运势增加免责声明：综合星级为固定值，事业/感情/财运按黄历宜忌关键词匹配，仅供娱乐和文化研究参考

## [1.0.0] — 首次发布（对应 PyPI `bach-lunar-mcp` 1.0.0）

### 新增

- 六个 MCP 工具：`bazi_calculate`（八字）、`calendar_convert`（历法转换）、`huangli_query`（黄历）、`fortune_daily`（每日运势）、`jieqi_query`（节气）、`wuxing_analyze`（五行分析）
- 一键启动入口 `uvx bach-lunar-mcp`（`[project.scripts]` 的 `bach-lunar-mcp = "server:main"`）
- 依赖 lunar-python、mcp、pydantic，要求 Python 3.12+
- MIT 许可证
