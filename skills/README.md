# Skills 目录

存放自定义 AI Skills 定义文件。

## 已有 Skills

### 从 Claude 金融插件转换的 Skills（skills/converted/）

| Skill | 说明 | 来源 |
|-------|------|------|
| [dcf-model](./converted/dcf-model/SKILL.md) | DCF 估值模型 — 机构级股权估值分析 | Anthropic financial-services |
| [earnings-analysis](./converted/earnings-analysis/SKILL.md) | 盈利分析报告 — 季度财报更新分析 | Anthropic financial-services |
| [comps-analysis](./converted/comps-analysis/SKILL.md) | 可比公司分析 — 同行估值基准研究 | Anthropic financial-services |
| [ic-memo](./converted/ic-memo/SKILL.md) | 投资委员会备忘录 — PE 项目审批文档 | Anthropic financial-services |
| [dd-checklist](./converted/dd-checklist/SKILL.md) | 尽职调查清单 — 全流程 DD 跟踪 | Anthropic financial-services |
| [merger-model](./converted/merger-model/SKILL.md) | 并购模型 — 增厚/稀释分析 | Anthropic financial-services |
| [financial-plan](./converted/financial-plan/SKILL.md) | 财务规划 — 退休/教育金/遗产规划 | Anthropic financial-services |
| [value-creation-plan](./converted/value-creation-plan/SKILL.md) | 价值创造计划 — 投后 100 天执行 | Anthropic financial-services |

### 总计：8 个已转换 Skill

| 方向 | Skill 数量 | 覆盖范围 |
|------|-----------|---------|
| 估值建模 | 3 | DCF、Comps、并购模型 |
| 投资分析 | 2 | IC备忘录、DD清单 |
| 财富管理 | 1 | 财务规划 |
| 投后管理 | 1 | 价值创造计划 |
| 研究报告 | 1 | 盈利分析报告 |

## Skill 结构

```
my-skill/
├── SKILL.md    # Skill 指令定义
├── assets/     # 资源文件（可选）
└── scripts/    # 脚本文件（可选）
```

## 创建新 Skill

参考 [Qoder Skills 文档](https://qoder.com/docs/skills) 创建自定义 Skill。

## 转换说明

来自 Claude 插件的 Skill 已做以下适配：
- 移除 Claude 特有 frontmatter（YAML `---` 头）
- 添加 Qoder 格式的「触发条件」「执行步骤」「输出规范」章节
- 保留原始领域知识和工作流细节
- 保持金融行业专业标准（WACC 计算、敏感性分析、数据来源要求等）
