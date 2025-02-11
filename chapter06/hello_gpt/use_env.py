import os
from typing import Any,Dict

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key:str = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

response:Dict[str,Any] = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":"受けるより与えることの方が幸せを感じるを英語に翻訳してください"
        }
    ]
)

print(response.choices[0].message.content)
