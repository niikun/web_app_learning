import os
from flask import Flask,request,redirect,url_for,send_from_directory
import numpy as np
from PIL import Image
from keras import models

UPLOAD_FOLDER = "./data/upload"
RAMEN_MODEL_FILE = "./data/ramen.keras"

LABELS = ["salt","soya_source","spicy","miso","chilled"]
IMG_W,IMG_H = 32,32

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

model = models.load_model(RAMEN_MODEL_FILE)

@app.route("/")
def root():
    return f""""
    <html><body>
    <h1>ラーメン画像の分類</h1>
    <div class="box file">
    <form action="/predict" method="post" enctype="multipart/form-data">
    <input type="file" name="file" class="file-label/><br>
    <input type="submit" value="分類" class="button is-primary"/>
    </form></div>
    </body></html>
    """

@app.route("/predict",methods=["POST"]) 
def upload_file():
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":