# AI Workflow

AI 工作流实践项目 — Coze 工作流搭建与 MCP 工具集成。

## 概述

本项目记录和分享 AI 工作流的搭建经验，涵盖：

- **Coze 工作流**：多步骤 AI 自动化流程设计
- **MCP 工具集成**：将外部工具接入 AI Agent
- **Prompt 工程**：提示词设计与优化
- **Hooks 配置**：事件驱动的自动化守卫
- **Skills 开发**：可复用的 AI 能力模块

## 项目内容

```
ai-workflow/
├── coze-workflows/           # Coze 工作流定义
│   └── smart-copy/           # 智能文案生成工作流
├── mcp-tools/                # MCP 工具集成示例
├── prompt-templates/         # Prompt 模板库
├── skills/                   # 自定义 Skills
│   ├── converted/            # 从Claude金融插件转换的Skills
│   │   ├── dcf-model/        # DCF估值模型
│   │   ├── earnings-analysis/ # 盈利分析报告
│   │   └── comps-analysis/   # 可比公司分析
│   └── README.md
└── README.md
```

## 智能文案生成工作流

一个 Coze 多步骤 AI 工作流，支持营销文案、产品描述、活动方案等场景。

### 工作流步骤

1. **意图理解** — 解析用户输入的文案需求
2. **知识检索** — 从知识库中检索行业案例
3. **内容生成** — LLM 生成初稿
4. **风格控制** — 按指定风格润色
5. **SEO 优化** — 优化关键词密度
6. **质量检查** — 自动校验输出质量

### 效果

- 生成质量稳定性提升 **60%**
- 人工修改率降低至 **20%**
- 日均生成文案 **200+** 篇

## MCP 工具集成

将 MCP Server 集成到 Coze 工作流中，实现：

- 实时数据查询（数据库 / API）
- 文件读写操作
- 外部服务调用

## 快速开始

```bash
# 安装 MCP SDK
pip install mcp

# 运行本地 MCP Server
python mcp-tools/example_server.py
```
