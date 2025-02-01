from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)
socketio = SocketIO(app)

# MongoDBのクライアントを作成
mongo_uri = "mongodb+srv://niikun:Test091505!@cluster0.5bk0a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client["SNS"]
messages_collection = db["messages"]

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on("load_messages")
def load_messages():
    messages = messages_collection.find().sort('\id',-1).limit(10)
    messages = list(messages)[::-1]
    emit('load all messages',messages_return)

@socketio.on('send message')
def send_message(message):
    message_collection.insert_one({"messsage":message})
    emit('load one message',message,broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)