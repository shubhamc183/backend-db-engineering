from app import handle_get, handle_post
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'output': handle_get(request)})


@app.route('/', methods=['POST'])
def post():
    return jsonify({'output': handle_post(request)})


if __name__ == '__main__':
    app.run()
