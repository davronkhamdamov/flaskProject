import random
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)

CORS(app)

items = [
    {'id': 1, 'name': 'Sarah Johnson'},
    {'id': 2, 'name': 'David Smith'},
    {'id': 3, 'name': 'Emily Brown'},
    {'id': 4, 'name': 'Michael Davis'},
    {'id': 5, 'name': 'Jessica Wilson'},
]


# Define a route to retrieve all items
@app.route('/', methods=['GET'])
def get_items():
    random.shuffle(items)
    return jsonify(items)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
