from flask import Flask,request,render_template
import davis_train_predict as dtp

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html><body>
    <h1>体重と身長から肥満を計算する</h1>
    <form action="/predict" method="get">
    身長: <input type="text" name="height"><br>
    体重: <input type="text" name="weight"><br>
    <input type="submit" value="計算">
    </form>
    </body></html>
    """

@app.route("/predict")
def predict():
    height = request.args.get("height")
    weight = request.args.get("weight")
    result = dtp.clf.predict([[height, weight]])[0]
    return f"""
    <html><body>
    <h1>あなたの肥満度は{result}です</h1>
    <a href="/">戻る</a>
    </body></html>
    """

if __name__ == "__main__":
    app.run(debug=True)