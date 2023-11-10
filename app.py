import random
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)

CORS(app)


@app.route('/', methods=['POST'])
def get_items():
    request_body = request.get_json()
    random.shuffle(request_body)
    return jsonify(request_body)


@app.route('/test', methods=['GET'])
def test():
    return "ok"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
