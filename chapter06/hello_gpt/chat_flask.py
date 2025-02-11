import os
from flask import Flask, request, render_template, redirect, url_for, session
from dotenv import load_dotenv  
from openai import OpenAI
import markdown
from typing import Any, Dict, List

load_dotenv()
openai_api_key: str = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

def initialize_session():
    if "messages" not in session:
        session["messages"] = [
            {
                "role": "system",
                "content": "あなたは子供向けにシンプルにわかりやすく教える大阪弁の先生です。",
            }
        ]

def append_session(role: str, content: str):
    messages: List = session["messages"]
    messages.append({
        "role": role,
        "content": content
    })
    session["messages"] = messages

def ask_chatgpt(user_input: str, model: str = "gpt-4o-mini") -> str:
    append_session("user", user_input)
    response: Dict[str, Any] = client.chat.completions.create(
        model=model,
        messages=session["messages"]
    )
    print("API Response:", response)  # デバッグ用にレスポンスを出力
    if response and "choices" in response and len(response["choices"]) > 0:
        gpt_answer = response["choices"][0]["message"]["content"]
        append_session("assistant", gpt_answer)
        return gpt_answer
    else:
        return "Error: No response from OpenAI API"

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")

@app.route("/")
def index():
    initialize_session()
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    user_input: str = request.form["user_input"]
    language: str = request.form["language"]
    user_question: str = f"「{user_input}」を{language}に翻訳してください。"
    translation_result = ask_chatgpt(user_question)
    return render_template("translation_result.html", translation_result=translation_result, user_input=user_input, language=language)

@app.route("/tokenize", methods=["POST"])
def tokenize():
    user_question: str = "翻訳結果を単語分割して、それぞれの単語の意味と発音を教えてください。"
    tokenization_result = ask_chatgpt(user_question)
    return render_template("tokenization_result.html", tokenization_result=tokenization_result)

if __name__ == "__main__":
    app.run(debug=True)