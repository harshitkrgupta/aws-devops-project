from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello Harshit 🚀, ENV = {os.getenv('ENV_NAME')}"

app.run(host='0.0.0.0', port=5000)
