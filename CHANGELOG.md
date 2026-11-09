# Changelog

本文件记录 `bach-lunar-mcp`（GitHub 仓库 `BACH-AI-Tools/lunar_mcp_server`）自 1.0.0 发布以来的变更。

标注约定：

- 「待合并」：对应改动已作为文档草稿/PR 通过审核，但尚未合并进 `main` 分支；
- 「未落地」：问题已确认并记录为 Issue，但修复代码尚未提交。

## [Unreleased] — 自 1.0.0 以来的变更

### 文档整改（已通过审核，待合并）

- **README.md / README.cn.md（中英双版）**：
  - 修正克隆命令为真实地址 `https://github.com/BACH-AI-Tools/lunar_mcp_server`，并更正目录名为 `lunar_mcp_server`（原占位符与旧目录名有误）
  - 启动命令由 `python -m src.server` 改为官方入口 `uvx bach-lunar-mcp`
  - 删除不存在的 `quick_test.py` / `run_server.py` 运行示例，并如实说明当前仓库暂无自动化测试
  - 开发依赖命令由 `uv add --dev …` 更正为 `uv sync --extra dev`
  - 直接使用示例的导入统一为 `from utils import LunarHelper`
  - 节气功能宣传整改：不再宣称「查询任意年份的完整 24 节气」，改为「查询指定年份的节气」并标注已知限制
  - 补全示例输出（如 2024-01-01 → 二〇二三年冬月二十）
- **QUICKSTART_UVX.md**：
  - 节气功能宣传整改（同 README，并删除「今年的立春是什么时候」示例）
  - 每日运势增加免责声明：综合星级为固定值，事业/感情/财运按黄历宜忌关键词匹配，仅供娱乐和文化研究参考
- **docs/FAQ.md（新增）**：15 条中英双语常见问题（安装、参数、报错与结果解读）
- **SECURITY.md（新增）**：安全漏洞上报渠道
- **.github/ISSUE_TEMPLATE/bug.yml（新增）**：Bug 上报模板（5 字段）

### 待修复（已确认，未落地）

- **节气查询返回不完整**（Issue #3）：`jieqi_query` 只检查每月 1 号，通常返回 0 条，无法返回完整 24 节气。
- **五行标签错误**（Issue #4）：黄历与运势把「日干支」显示为「五行」，幸运方位/颜色为占位文案。
- **锁文件不同步**（Issue #5）：`uv.lock` 的包名与 `mcp` 依赖约束和 `pyproject.toml` 不一致。
- **闰月显示负数**（Issue #6）：公历转农历时，闰月的农历月份显示为负数。

## [1.0.0] — 首次发布（对应 PyPI `bach-lunar-mcp` 1.0.0）

### 新增

- 六个 MCP 工具：`bazi_calculate`（八字）、`calendar_convert`（历法转换）、`huangli_query`（黄历）、`fortune_daily`（每日运势）、`jieqi_query`（节气）、`wuxing_analyze`（五行分析）
- 一键启动入口 `uvx bach-lunar-mcp`（`[project.scripts]` 的 `bach-lunar-mcp = "server:main"`）
- 依赖 lunar-python、mcp、pydantic，要求 Python 3.12+
- MIT 许可证