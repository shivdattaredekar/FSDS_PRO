from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "users": [
        {"id": 1, "name": "shiv", "email": "shiv@example.com"},
        {"id": 2, "name": "bobby", "email": "bobby@example.com"},
        {"id": 3, "name": "ramesh", "email": "ramesh@example.com"}
    ]
}

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
