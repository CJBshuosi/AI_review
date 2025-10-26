import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("DEEPSEAK_API"), base_url="https://api.deepseek.com")

def ask_model(prompt: str) -> str:
    """
    Use OpenAI gpt-5-mini to perform the code review.
    """
    response = client.chat.completions.create(
        model="deepseek-coder",  # ✅ 最优模型，可改为 gpt-4o-mini 节省费用
        messages=[
            {"role": "system", "content": "You are a professional AI code reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1200,
    )

    return response.choices[0].message.content.strip()