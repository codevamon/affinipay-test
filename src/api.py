from flask import Flask, request, jsonify
import json

app = Flask(__name__)
data_store = {}

@app.route('/dogs/<dog_id>', methods = ['GET', 'DELETE', 'PUT', 'PATCH', 'POST'])
def dogs_slash_id(dog_id):
    if request.method == 'GET':
        if dog_id in data_store.keys():
            return jsonify(data_store[dog_id]), 200
        else:
            return "Doggo Not Found", 404
    if request.method == 'DELETE':
        if dog_id in data_store.keys():
            data = data_store.pop(dog_id)
            return jsonify(data), 200
        else:
            return "Doggo Not Found", 404
    else:
        return "Woof! Method Not Allowed", 405

@app.route("/dogs/", methods = ['GET', 'DELETE', 'PUT', 'PATCH', 'POST'])
def dogs():
    if request.method == 'GET':
        return(data_store, 200)
    if request.method == 'POST':
        request_data = request.get_json()
        if check_payload(request_data):
            new_index = str(len(data_store.keys()) + 1)
            request_data['id']=new_index
            data_store[new_index]=request_data
            return jsonify(request_data), 200
        else:
            return "Invalid Doggy Payload", 422
    else:
        return("Woof! Method Not Allowed", 405)

@app.route('/', methods = ['GET', 'DELETE', 'PUT', 'PATCH', 'POST'])
def slash():
    if request.method == 'POST':
	    return('Ru Roh Raggy, This should\'nt have succeeded', 200)
    else:
        return("Woof! Method Not Allowed", 405)



def check_payload(payload):
    if("name" in payload.keys()) and ("breed" in payload.keys()) and ("age" in payload.keys()):
        return  (type(payload['name']) == str) and (type(payload['age']) == int) and (type(payload['breed']) == str)
    else:
        return false


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)