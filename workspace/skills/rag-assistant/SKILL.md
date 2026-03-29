---
name: rag-assistant
description: Use this skill only when the user explicitly includes [USE_RAG]. This skill is for local algorithm RAG queries and should call the local RAG client through exec.
---

# Local RAG Study Assistant

This skill is only for the local algorithm RAG service.

## When to use this skill

Use this skill ONLY when the user message contains:

[USE_RAG]

Typical requests:
- algorithm problem matching
- LeetCode / Hot100 similarity lookup
- knowledge point identification
- study suggestions for an algorithm problem
- wrong-question analysis for algorithm exercises

Examples:
- [USE_RAG] 给定数组找三个数之和等于0
- [USE_RAG] 这题最像哪道 LeetCode
- [USE_RAG] 这题应该练什么知识点

## When NOT to use this skill

Do NOT use this skill if the message does not contain [USE_RAG].

Do NOT use this skill for:
- normal chat
- Git / Python / environment setup questions
- nanobot configuration questions
- FastAPI debugging
- MCP explanations
- general coding explanations unrelated to local algorithm retrieval

## Required behavior

If [USE_RAG] is present:

1. Remove the prefix [USE_RAG]
2. Extract the user's actual query
3. MUST call the local RAG client through exec
4. Use the tool result as the primary source of truth
5. Prefer the answer field in the returned JSON
6. If available, also include source and trace_id
7. If the tool fails, clearly say the local RAG tool failed

If [USE_RAG] is NOT present:

- DO NOT call the local RAG client
- DO NOT pretend to use the local RAG tool

## Command

Use exec to run:

python tools/rag_http_query.py --query "<USER_QUERY>"

Replace <USER_QUERY> with the user's actual query after removing [USE_RAG].

## Output rules

- Never claim the tool was used unless it was actually executed
- Never invent a LeetCode problem if the tool result does not support it
- Never answer from general knowledge first when [USE_RAG] is present
- If the output is invalid or missing fields, say so clearly

## Preferred response format

[RAG回答]
<answer>

source: <source if available>
trace_id: <trace_id if available>