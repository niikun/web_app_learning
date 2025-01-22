from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>これは掲示板のトップページです</h1>"

# @app.route("/write",methods=["GET"])
# def write_by_get_method():
#     return """
#         <html><body>
#             <h1>新しい記事を書きます</h1>
#                 <p>記事を書くためのフォームを表示します</p>
#                 <form action="/write" method="POST">
#                     <input type="text" name="title" placeholder="タイトル">
#                     <textarea name="content" placeholder="本文"></textarea>
#                     <input type="submit" value="送信">
#                 </form>
#         </body></html>"""

# @app.route("/write",methods=["POST"])
# def write_by_post_method():
#     title = request.form.get("title")
#     content = request.form.get("content")
#     return f"""
#     <h1>以下の文章を書き込みます。</h1>
    # <h1>タイトル:{title}</h1><p>{content}</p>"""

@app.route("/write",methods=["GET","POST"])
def write():
    if request.method == "GET":
        return """
            <html><body>
                <h1>新しい記事を書きます</h1>
                    <p>記事を書くためのフォームを表示します</p>
                    <form action="/write" method="POST">
                        <input type="text" name="title" placeholder="タイトル">
                        <textarea name="content" placeholder="本文"></textarea>
                        <input type="submit" value="送信">
                    </form>
            </body></html>"""
    else:
        title = request.form.get("title")
        content = request.form.get("content")
        return f"""
        <h1>以下の文章を書き込みます。</h1>
        <h1>タイトル:{title}</h1><p>{content}</p>"""
      

@app.route("/edit/<int:message_id>")
def edit(message_id):
    return f"<h1>記事{type(message_id).__name__}を編集します</h1>"


if __name__ == "__main__":
    app.run(debug=True)