from flask import Flask,request,render_template

app = Flask(__name__)

class Message:
    def __init__(self,id:str,user_name:str,contents:str):
        self.id = id
        self.user_name = user_name
        self.contents = contents


@app.route("/")
def index():
    login_user_name = "niikun"
    message_list = [
        Message("1","niikun","こんにちは！"),
        Message("2","sankun","こんばんは！"),
        Message("3","yonkun","おはよう！")
    ]

    return render_template("top.html",
                           login_user_name=login_user_name,
                           message_list=message_list
        )


@app.route("/write")
def write():
    return render_template("write.html")

if __name__=="__main__":
    app.run(debug=True)