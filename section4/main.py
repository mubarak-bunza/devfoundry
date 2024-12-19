from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    welcome_msg = os.getenv("WELCOME_MSG", "Default")
    return f"{welcome_msg}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)