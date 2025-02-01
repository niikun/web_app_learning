from flask import Flask, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import escape

app:Flask = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memo.db"
db:SQLAlchemy = SQLAlchemy(app)

class MemoItem(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    title:str = db.Column(db.Text,nullable=False)
    body:str = db.Column(db.Text,nullable=False)

with app.app_context():
    db.create_all()

# HTMLを定義

CSS = "https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"
HTML_HEADER = f"""
<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="{CSS}"></head>
<body class="p-3">
<h1 class="has-background^inf p-3 mb-3">Memo App</h1>
"""

HTML_EDITOR_FORM = """
<div class="card p-3">
<form method="POST">
<label class="label">Title</label>
<input type="text" name="title" value="{title}" class="input">
<label class="label">本文</label>
<textarea name="body" class="textarea">{body}</textarea>
<input type="submit" value="保存" class="button is-primary">
</form></div>
"""

HTML_FOOTER = """
</body></html>
"""

@app.route("/",methods=["GET","POST"])
def index():
    it = MemoItem.query.get(1)
    if it is None:
        it = MemoItem(id=1,title="無題",body="")
        db.session.add(it)
        db.session.commit()

    if request.method == "POST":
        it.title = request.form.get("title")
        it.body = request.form.get("body")
        if it.title == "":
            return "タイトルは空にできません。"
        db.session.commit()
        return redirect(url_for("index"))
    
    title,body = escape(it.title),escape(it.body)
    edit = HTML_EDITOR_FORM.format(title=title,body=body)
    html = HTML_HEADER + edit + HTML_FOOTER
    return html

if __name__ == "__main__":
    app.run(debug=True,port=8888)