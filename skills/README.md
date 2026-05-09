# Skills 目录

存放自定义 AI Skills 定义文件。

## 已有 Skills

### 从 Claude 金融插件转换的 Skills（skills/converted/）

| Skill | 说明 | 来源 |
|-------|------|------|
| [dcf-model](./converted/dcf-model/SKILL.md) | DCF 估值模型 — 机构级股权估值分析 | Anthropic financial-services |
| [earnings-analysis](./converted/earnings-analysis/SKILL.md) | 盈利分析报告 — 季度财报更新分析 | Anthropic financial-services |
| [comps-analysis](./converted/comps-analysis/SKILL.md) | 可比公司分析 — 同行估值基准研究 | Anthropic financial-services |

### Qoder 原生 Skills

- （待添加）

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
