# Tool Usage Notes

Tool signatures are provided automatically via function calling.
This file documents non-obvious constraints and usage patterns.

## exec — Safety Limits

- Commands have a configurable timeout (default 60s)
- Dangerous commands are blocked (rm -rf, format, dd, shutdown, etc.)
- Output is truncated at 10,000 characters


## cron — Scheduled Reminders

- Please refer to cron skill for usage.


## RAG — Study Assistant

The local RAG tool is only for the user's local algorithm study assistant.

Use it ONLY when the user's message explicitly contains:

[USE_RAG]

If [USE_RAG] is present:
- remove the prefix
- extract the actual query
- call the local RAG client via exec
- use the tool result as the primary answer

If [USE_RAG] is NOT present:
- do not call the local RAG tool
- do not mention the local RAG tool
- answer normally

Command to run:

python tools/rag_http_query.py --query "<USER_QUERY>"

Important:
- Never pretend the tool was used
- Never invent tool errors
- Do not claim localhost is blocked unless there is an actual execution error showing that
- If exec succeeds, trust the returned result