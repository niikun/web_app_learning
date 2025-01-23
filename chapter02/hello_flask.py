from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    age:int=19
    return "<p>貴方の年齢は" + str(age) +"です</p>"


if __name__ == "__main__":
    app.run(debug=True)