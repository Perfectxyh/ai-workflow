"""
智能文案生成工作流 — MCP Server 示例

为 Coze 工作流提供 MCP 工具接口，支持文案生成、风格控制等功能。
"""

import json
import sys
import random
from datetime import datetime

# 文案模板库
COPY_TEMPLATES = {
    "营销文案": {
        "prefix": "🔥 限时特惠！",
        "suffix": "立即抢购，错过今天再等一年！",
        "style_tags": ["紧迫感", "促销", "行动号召"]
    },
    "产品描述": {
        "prefix": "【新品上市】",
        "suffix": "匠心品质，值得信赖。",
        "style_tags": ["专业", "详细", "品质"]
    },
    "活动方案": {
        "prefix": "🎉 精彩活动来袭！",
        "suffix": "诚邀您的参与，共度美好时光。",
        "style_tags": ["热情", "邀请", "互动"]
    }
}

STYLES = ["正式", "轻松", "幽默", "专业", "热情", "简洁"]


def handle_request(request: dict) -> dict:
    method = request.get("method", "")
    params = request.get("params", {})
    req_id = request.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "protocolVersion": "2025-03-26",
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "ai-workflow-tools", "version": "1.0.0"}
            }
        }

    elif method == "tools/list":
        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "generate_copy",
                        "description": "根据主题和类型生成文案",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "topic": {"type": "string", "description": "文案主题"},
                                "copy_type": {
                                    "type": "string",
                                    "description": "文案类型",
                                    "enum": list(COPY_TEMPLATES.keys())
                                },
                                "style": {
                                    "type": "string",
                                    "description": "文案风格",
                                    "enum": STYLES
                                }
                            },
                            "required": ["topic", "copy_type"]
                        }
                    },
                    {
                        "name": "list_templates",
                        "description": "列出可用的文案模板类型",
                        "inputSchema": {"type": "object", "properties": {}}
                    },
                    {
                        "name": "optimize_seo",
                        "description": "优化文案中的SEO关键词",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string", "description": "待优化的文案"},
                                "keywords": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "目标关键词列表"
                                }
                            },
                            "required": ["text", "keywords"]
                        }
                    }
                ]
            }
        }

    elif method == "tools/call":
        tool_name = params.get("name", "")
        args = params.get("arguments", {})

        if tool_name == "generate_copy":
            topic = args.get("topic", "默认主题")
            copy_type = args.get("copy_type", "营销文案")
            style = args.get("style", "专业")

            template = COPY_TEMPLATES.get(copy_type, COPY_TEMPLATES["营销文案"])
            body = f"{topic} —— 这是由AI生成的{copy_type}内容。"
            result = f"{template['prefix']}{body}{template['suffix']}"

            return {
                "jsonrpc": "2.0", "id": req_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps({
                            "title": f"{topic} — {copy_type}",
                            "content": result,
                            "style": style,
                            "tags": template["style_tags"],
                            "generated_at": datetime.now().isoformat()
                        }, ensure_ascii=False)
                    }]
                }
            }

        elif tool_name == "list_templates":
            return {
                "jsonrpc": "2.0", "id": req_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(list(COPY_TEMPLATES.keys()), ensure_ascii=False)
                    }]
                }
            }

        elif tool_name == "optimize_seo":
            text = args.get("text", "")
            keywords = args.get("keywords", [])
            optimized = text
            for kw in keywords:
                if kw not in optimized:
                    optimized += f" #{kw}"
            return {
                "jsonrpc": "2.0", "id": req_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps({
                            "original": text,
                            "optimized": optimized,
                            "keywords_used": keywords,
                            "keyword_count": len(keywords)
                        }, ensure_ascii=False)
                    }]
                }
            }

    return {
        "jsonrpc": "2.0", "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"}
    }


def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            response = handle_request(json.loads(line.strip()))
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0", "id": None,
                "error": {"code": -32603, "message": str(e)}
            }
            sys.stdout.write(json.dumps(error_response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
