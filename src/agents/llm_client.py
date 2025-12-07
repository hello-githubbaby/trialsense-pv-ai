"""
Minimal LLM client abstraction.

- Works offline using a placeholder response.
- If OPENAI_API_KEY is set, it attempts a real LLM call.
"""

import os

def call_llm(prompt: str, max_tokens: int = 512):
    api_key = os.getenv("OPENAI_API_KEY")

    # Real LLM mode
    if api_key:
        try:
            import openai
            openai.api_key = api_key

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )

            return response["choices"][0]["message"]["content"]

        except Exception as e:
            return f"[LLM error: {e}]"

    # Offline fallback mode
    return f"[LLM placeholder response]\nPROMPT:\n{prompt[:1000]}"
