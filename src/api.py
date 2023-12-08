from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
	user_data = {
        "user_id": '1234',
        "name": "Testy McTesterton",
        "email": "foo@bar.com"
    }
	return jsonify(user_data), 200

@app.route("/<user_id>", methods=['GET'])
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Testy McTesterton",
        "email": "foo@bar.com"
    }
    return jsonify(user_data), 200




if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)