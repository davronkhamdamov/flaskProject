import random
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)

CORS(app)

items = [
    {'id': 1, 'name': 'First'},
    {'id': 2, 'name': 'Second'},
    {'id': 3, 'name': 'Third'},
    {'id': 4, 'name': 'Fourth'},
    {'id': 5, 'name': 'Fifth'},
]


# Define a route to retrieve all items
@app.route('/', methods=['GET'])
def get_items():
    random.shuffle(items)
    return jsonify(items)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
