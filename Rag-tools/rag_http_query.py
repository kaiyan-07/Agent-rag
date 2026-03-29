import argparse
import json
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, help="用户问题")
    parser.add_argument("--top_k", type=int, default=3)
    parser.add_argument("--model_name", default="llama3")
    parser.add_argument("--url", default="http://127.0.0.1:8000/ask")
    args = parser.parse_args()

    payload = {
        "query": args.query,
        "top_k": args.top_k,
        "model_name": args.model_name,
    }

    try:
        response = requests.post(args.url, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except requests.RequestException as e:
        error_result = {
            "success": False,
            "error": str(e),
            "source": "LOCAL_RAG_HTTP_CLIENT"
        }
        print(json.dumps(error_result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()