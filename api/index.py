from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/hello")
def hello_world():
    return jsonify({
        'message': 'Hello, World!',
    })

@app.route('/api/home', methods=['GET'])
def return_home():
    return jsonify({
        'message': 'Welcome to the home page',
    })