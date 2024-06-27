# app.py for client
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "привет сооискатель1"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
