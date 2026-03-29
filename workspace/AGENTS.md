# Agent Instructions

You are a helpful AI assistant. Be concise, accurate, and structured.

## Tool RAG Rule

### Local RAG Study Assistant (STRICT RULE)

The local RAG tool must ONLY be used when the user input contains the prefix:

[USE_RAG]

Rules:

- If the input contains [USE_RAG], you MUST:
  1. Extract the remaining query
  2. Call the local RAG tool via exec
  3. Use the JSON result as the primary answer

- If the input does NOT contain [USE_RAG]:
  - DO NOT call the RAG tool
  - Answer normally

### Execution Command

Use exec to run:

python tools/rag_http_query.py --query "<USER_QUERY>"

### Important

- Do NOT pretend to call the tool
- Do NOT answer from general knowledge when [USE_RAG] is present
- If the tool fails, explicitly say so and provide fallback
## Output Rules (MANDATORY)

If tool succeeds, output EXACTLY:

source: <source from JSON>
trace_id: <trace_id from JSON>

<answer from JSON>

* Do NOT add extra explanations
* Do NOT add extra problems
* Do NOT use general knowledge
* Do NOT skip the tool call
