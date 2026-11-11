# 常见问题 / Frequently Asked Questions

> 本文档由项目维护团队根据代码与仓库现状整理，用于排查 `bach-lunar-mcp`（仓库 `lunar_mcp_server`）的使用问题。
> This FAQ is maintained by the project maintainers and verified against the source code and repository.

## 环境与启动 / Setup & Launch

### 1. 需要什么运行环境？
**What runtime environment is required?**

**答：** Python 3.12+（见 `pyproject.toml:10`）。通过 `uvx bach-lunar-mcp` 一键运行时无需手动安装依赖，uv 会自动下载并运行。本地从源码运行则需要 Python 3.12+ 和 uv。

**A:** Python 3.12+ (see `pyproject.toml:10`). With `uvx bach-lunar-mcp` no manual dependency installation is needed; uv downloads and runs the package. Running from source requires Python 3.12+ and uv.

### 2. 为什么 `uvx bach-lunar-mcp` 启动后看不到任何日志输出？
**Why does `uvx bach-lunar-mcp` print nothing after starting?**

**答：** 这是正常现象。MCP 服务器通过 stdio 与客户端通信，stdout 被用于传输 MCP 协议消息；本项目代码中没有 print / logging 日志输出（`src/server.py` 全文无 print 语句）。所以「静默运行」不代表出错，只要客户端能正常列出工具即可。

**A:** This is expected. The MCP server talks to clients over stdio, so stdout is reserved for MCP protocol messages. The code has no print/logging output (no `print` statements in `src/server.py`). Quiet startup is not a failure — as long as the client can list the tools, the server is working.

### 3. 客户端里看不到任何工具，该查什么？
**The client shows no tools — what should I check?**

**答：** 依次检查：① `uvx` 是否在 PATH 中、能否直接运行；② MCP 客户端配置里的命令是否为 `uvx`、参数是否为 `["bach-lunar-mcp"]`（参考 `README.md` 各客户端配置示例）；③ 服务器是否正常启动（配置正确时会静默运行，见第 2 条）。

**A:** Check in order: ① whether `uvx` is on PATH and runnable; ② whether the client config uses `command: "uvx"` and `args: ["bach-lunar-mcp"]` (see the client examples in `README.md`); ③ whether the server actually started (a correct config runs quietly — see item 2).

### 4. PyPI 包名、仓库名、启动命令为什么不一样？
**Why do the PyPI package name, repository name, and launch command differ?**

**答：** PyPI 包名是 `bach-lunar-mcp`（`pyproject.toml:6`），GitHub 仓库名是 `lunar_mcp_server`，`uvx` 使用的是 PyPI 包名。克隆仓库后要 `cd` 进的是 `lunar_mcp_server` 目录，不是 `lunar-mcp-server`。

**A:** The PyPI package is `bach-lunar-mcp` (`pyproject.toml:6`), while the GitHub repo is `lunar_mcp_server`; `uvx` uses the PyPI package name. After cloning, `cd` into `lunar_mcp_server`, not `lunar-mcp-server`.

## 参数与报错 / Parameters & Errors

### 5. 日期格式写错为什么会报 "list index out of range"？
**Why does a wrong date format produce "list index out of range"?**

**答：** 工具按 `-` 分割日期字符串并取三段（如 `src/server.py:32-35`、`:162-163`）。若传入 `2024/01/01`（斜杠）或 `2024-1`（缺段），分割后索引越界，异常被捕获后显示的就是 `list index out of range`。请始终使用 `YYYY-MM-DD` 格式。

**A:** The tools split the date string by `-` and index three parts (e.g. `src/server.py:32-35`, `:162-163`). Passing `2024/01/01` (slashes) or `2024-1` (missing part) causes an index error, which is caught and reported as `list index out of range`. Always use `YYYY-MM-DD`.

### 6. 为什么提示 "Missing date parameter"？
**Why do I see "Missing date parameter"?**

**答：** 当模型没有把日期参数传给工具时，`huangli_query` 等会直接返回该提示（`src/server.py:158-159`；`fortune_daily` 见 `:219-220`）。在提问里明确写出日期（如「2024年10月1日」）通常即可解决。

**A:** When the model does not pass a date argument, tools like `huangli_query` return this message (`src/server.py:158-159`; `fortune_daily` at `:219-220`). Spelling out the date in the prompt (e.g. "October 1, 2024") usually fixes it.

### 7. 农历转公历时闰月怎么传？
**How do I pass a leap month when converting lunar to solar?**

**答：** `calendar_convert` 有 `is_leap` 参数（`src/server.py:75`）。农历转公历且目标月份是闰月时，把 `is_leap` 设为 `true`；内部用负数月表示闰月（`src/utils/lunar_helper.py:81-82`）。

**A:** `calendar_convert` has an `is_leap` parameter (`src/server.py:75`). When converting lunar→solar for a leap month, set `is_leap: true`; internally a leap month is represented by a negative month number (`src/utils/lunar_helper.py:81-82`).

### 8. `birth_time` 只写小时可以吗？
**Is it OK to provide only the hour for `birth_time`?**

**答：** 可以。`HH` 会被当作 `HH:00`：分钟缺省时补 0（`src/server.py:36`、`:332`）。建议尽量写全 `HH:MM` 以减少歧义。

**A:** Yes. `HH` is treated as `HH:00` — the minute defaults to 0 when missing (`src/server.py:36`, `:332`). Providing full `HH:MM` is recommended to avoid ambiguity.

## 结果解读 / Reading the Results

### 9. 为什么 `jieqi_query` 查任何年份都返回 0 个节气？
**Why does `jieqi_query` return 0 solar terms for any year?**

**答：** 当前实现只检查每个公历月的 1 号是否是节气（`src/utils/lunar_helper.py:216-229`），而节气通常落在每月 4-8 日或 19-23 日，所以几乎不会命中，返回列表通常为空。已记录为 [Issue #3](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/3)，修复前该功能不可用。

**A:** The current implementation only checks the 1st of each Gregorian month (`src/utils/lunar_helper.py:216-229`), but solar terms usually fall on the 4th-8th or 19th-23rd, so the list is almost always empty. Tracked as [Issue #3](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/3); the feature is unusable until fixed.

### 10. 黄历里的「五行」为什么显示的是干支？运势的方位、颜色是真实数据吗？
**Why does "Wu Xing" in the almanac show Gan-Zhi? Are the fortune direction/color real data?**

**答：** 黄历输出的「五行」字段实际填的是当日干支（如「丙寅」），不是金木水火土（`src/utils/lunar_helper.py:189`、`src/server.py:194`）；运势里的「方位」「颜色」是模板占位文案（`src/server.py:248-249`）。已记录为 [Issue #4](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/4)，待修复。

**A:** The "Wu Xing" field in the almanac actually holds the day's Gan-Zhi (e.g. 丙寅), not the five elements (`src/utils/lunar_helper.py:189`, `src/server.py:194`); the fortune "direction" and "color" are placeholder text (`src/server.py:248-249`). Tracked as [Issue #4](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/4), pending fix.

### 11. 八字计算会做时区或真太阳时换算吗？
**Does BaZi calculation apply timezone or true solar time correction?**

**答：** 不会。八字直接使用传入的日期时间（`src/utils/lunar_helper.py:118`），不做时区或真太阳时校正。需要精确排盘时，请先自行把时间换算到目标时区再传入。

**A:** No. BaZi uses the given date/time as-is (`src/utils/lunar_helper.py:118`) with no timezone or true solar time correction. For precise charts, convert the time to the desired timezone before passing it in.

## 其他 / Others

### 12. 不接 MCP 客户端，能直接在代码里调用吗？
**Can I use the helper functions directly without an MCP client?**

**答：** 可以。在仓库根目录下运行：`uv run python -c "from src.utils import LunarHelper; print(LunarHelper.solar_to_lunar(2024, 1, 1)['lunar_date_chinese'])"`（`src/utils/__init__.py:8` 已导出 `LunarHelper`，完整示例见 `README.md:136-147`）。

**A:** Yes. From the repo root: `uv run python -c "from src.utils import LunarHelper; print(LunarHelper.solar_to_lunar(2024, 1, 1)['lunar_date_chinese'])"` (`LunarHelper` is re-exported at `src/utils/__init__.py:8`; full examples at `README.md:136-147`).

### 13. README 里说的 `quick_test.py`、`run_server.py` 在哪？
**Where are `quick_test.py` and `run_server.py` mentioned in the README?**

**答：** 这两个脚本并不在仓库中，当前 README 里引用它们的命令已过时（`README.md:261`、`:264`）。要在本地启动服务器，用 `uv run python -m src.server`（入口 `main()` 在 `src/server.py:392-395`）。

**A:** These scripts do not exist in the repository; the README commands that reference them are outdated (`README.md:261`, `:264`). To run the server locally, use `uv run python -m src.server` (entry point `main()` at `src/server.py:392-395`).

### 14. `uv.lock` 和 `pyproject.toml` 不同步会影响使用吗？
**Does the `uv.lock` / `pyproject.toml` mismatch affect usage?**

**答：** 锁文件里的项目名还是旧名 `lunar-mcp-server`、mcp 版本约束也不一致（`uv.lock:192`、`:215` 对比 `pyproject.toml:6`、`:24`）。这主要影响从仓库执行 `uv sync` 的贡献者和 CI（可能锁定失败或装错版本）；`uvx bach-lunar-mcp` 的终端用户不受影响。已记录为 [Issue #5](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/5)。

**A:** The lock file still uses the old project name `lunar-mcp-server` and a different `mcp` constraint (`uv.lock:192`, `:215` vs `pyproject.toml:6`, `:24`). This mainly affects contributors/CI running `uv sync` from the repo (lock may fail or resolve wrong versions); end users of `uvx bach-lunar-mcp` are unaffected. Tracked as [Issue #5](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/5).

### 15. 年份参数有范围校验吗？
**Is the year parameter range-checked?**

**答：** 没有。`jieqi_query` 的 `year` 接受任意整数（`src/server.py:270`），代码未做范围校验，非法年份可能返回错误或空结果。当前该功能因 [Issue #3](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/3) 本来也查不出节气，建议等修复后再使用。

**A:** No. `jieqi_query` accepts any integer `year` (`src/server.py:270`) with no range validation; invalid years may return an error or empty result. Since the feature is blocked by [Issue #3](https://github.com/BACH-AI-Tools/lunar_mcp_server/issues/3), it is best to wait for the fix.

---

## 维护说明 / Maintenance note

本文档引用的 README（中/英）与 QUICKSTART 行号基于 2026-10-22 的仓库状态。待 README 与 QUICKSTART 的文档修改 PR 合并落地后，相关行号会漂移，届时需逐条回填核对一遍（受影响的主要是第 3、12、13 条引用的 README 行号，以及各条目中引用的 `README.md`/`QUICKSTART_UVX.md` 位置）。
