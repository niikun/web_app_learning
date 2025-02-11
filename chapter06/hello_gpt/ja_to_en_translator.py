import os
from typing import Any,Dict,List

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key:str = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

messages:List[Dict[str,str]] = [
    {
        "role":"system",
        "content":"あなたは子供向けにシンプルにわかりやすく教える大阪弁の先生です。",
    },
]

def ask_chatgpt(user_question:str,model:str="gpt-4o-mini") -> str:
    messages.append({
        "role":"user",
        "content":user_question
    })
    response:Dict[str,Any] = client.chat.completions.create(
        model=model,
        messages=messages
    )

    gpt_answer = response.choices[0].message.content

    messages.append({
        "role":"assistant",
        "content":gpt_answer
    })

    return gpt_answer

if __name__=="__main__":
    print("******英語に翻訳してほしい文章を日本語で入力してください******")
    user_input:str = input("日本語>")
    user_question:str = f"「{user_input}」を英語に翻訳してください。"
    print("回答>",ask_chatgpt(user_question))

    print("******さらに、単語分割の結果を知りたいですか？（1:知りたい、2:不要)******")
    user_input:str = input("1:知りたい、2:不要>")
    if user_input=="1":
        user_question:str = "翻訳結果を単語分割して、それぞれの単語の意味と発音を教えてください。"
        print("回答>",ask_chatgpt(user_question,model="gpt-4o-mini"))
    else:
        print("終了します。")
        quit()
