from flask import Flask, jsonify

app = Flask(__name__)

# Example users data
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    # Return the list of usernames in JSON format
    return jsonify(list(users.keys()))

if __name__ == "__main__":
    app.run(debug=True)

