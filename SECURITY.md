# Security Policy / 安全策略

本文件说明如何向 `lunar_mcp_server`（PyPI 包名 `bach-lunar-mcp`）的维护者报告安全漏洞。

This document explains how to report a security vulnerability in
`lunar_mcp_server` (PyPI package `bach-lunar-mcp`) to its maintainers.

## 报告安全漏洞 / Reporting a Vulnerability

如果你发现了疑似安全漏洞，请**私下**告诉我们，不要先在公开 Issue、PR 或讨论区贴出漏洞细节，以便我们在公开披露前完成修复。

If you have found a security vulnerability, please report it to us **privately**.
Do not post exploit details in public issues or discussions before we have a
chance to fix them.

### 上报渠道 / How to report

请从下面两种渠道中选一种，不要重复上报：

1. **GitHub Security Advisory（首选）**
   打开本仓库的 **Security** 标签页，点击 **Report a vulnerability**（若已开启私有漏洞报告）。这会创建一个只有维护者可见的私有安全通告。

2. **Issue 标注 `security`（备选）**
   若私有漏洞报告功能不可用，请新建一个 Issue，标题以 `[security]` 开头，例如 `[security] 某功能存在 XX 风险`。正文里**不要**写完整的利用代码或真实凭据，只描述影响和大致位置，并注明可以私下提供细节。

> 请在公开场合只做最低限度的描述；可被直接利用的细节（PoC、真实数据、密钥等）请通过私有渠道提供。

### 报告内容建议 / What to include

- 漏洞的简短描述及可能造成的影响；
- 受影响的版本（如 `1.0.0`）；
- 复现步骤（不要包含敏感数据）；
- 你建议的修复方式或临时规避方法（如有）。

### 处理流程 / What happens next

- 维护者会尽快确认收到你的报告；
- 我们会在修复并协调好披露节奏后再公开细节；
- 请给我们合理的时间完成修复，再进行公开披露。

### 范围 / Scope

本策略适用于 `lunar_mcp_server` 代码库及其发布的 PyPI 包 `bach-lunar-mcp`。
上游依赖（如 `lunar-python`）的漏洞请报告给对应项目的维护者。

## 支持版本 / Supported Versions

| 版本 / Version | 是否支持 / Supported |
| -------------- | -------------------- |
| 1.0.0          | ✅                   |
