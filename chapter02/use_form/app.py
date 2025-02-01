from datetime import datetime

from flask import Flask,request,render_template


class Message:
    def __init__(self, id:str,user_name:str,contents:str):
        self.id = id
        self.user_name = user_name
        self.contents = contents

app = Flask(__name__)
login_user_name = "niikun"

message_list = [
    Message("1","niikun","Hello"),
    Message("2","niikun","World"),
    Message("3","niikun","Good"),
]

@app.route("/")
def index():
    search_word :str = request.args.get("search_words")
    if search_word is None:
        return render_template("top.html",
                           login_user_name=login_user_name,
                           message_list=message_list
                           )
    else:
        search_result:list[Message] = [message for message in message_list if search_word in message.contents]
        return render_template("top.html",
                           login_user_name=login_user_name,
                           message_list=search_result
                           )
    

@app.route("/write",methods=["GET","POST"])
def write():
    if request.method == "GET":
        return render_template("write.html",login_user_name=login_user_name)
    elif request.method == "POST":
        id:str = datetime.now().strftime("%Y-%m%d-%H%M%S")
        user_name:str = request.form.get("user_name")
        contents:str = request.form.get("contents")
        if contents:
            message_list.insert(0,Message(id,user_name,contents))
        return render_template("top.html",login_user_name=login_user_name,message_list=message_list)

if __name__ == "__main__":
    app.run(debug=True)