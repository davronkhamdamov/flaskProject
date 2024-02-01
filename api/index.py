import random
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)

CORS(app)


@app.route('/random', methods=['POST'])
def get_items():
    request_body = request.get_json()

    if not request_body or not isinstance(request_body, list):
        return jsonify({'error': 'Invalid input. Expected a JSON array.'}), 400
    
    random.shuffle(request_body)
    return jsonify(request_body)

@app.route('/test', methods=['GET'])
def test():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)
