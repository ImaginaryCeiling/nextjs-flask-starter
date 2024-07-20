from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#127.0.0.1/5328

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def return_home():
    return jsonify({
        'message': 'Welcome to the home page',
    })

@app.route("/api/hello")
def hello_world():
    return jsonify({
        'message': 'Hello, World!',
    })


@app.route('/api/test', methods=['GET'])
def return_test():
    return jsonify({
        'message': 'Welcome to the test page',
    })

@app.route('/api/capitalize/<string>', methods=['GET'])
def capitalize_string(string):
    return jsonify({
        'message': string.capitalize(),
    })

if __name__ == "__main__":
    app.run(debug=True, port=5328)

 