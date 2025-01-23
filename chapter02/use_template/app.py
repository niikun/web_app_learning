from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    login_user_name = "niikun"
    return render_template("top.html",login_user_name=login_user_name)


@app.route("/write")
def write():
    return render_template("write.html")

@app.route("/edit/<int:message_id>")
def edit(message_id):
    return render_template("edit.html",message_id=message_id)

if __name__ == "__main__":
    app.run(debug=True)