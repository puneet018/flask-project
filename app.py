from flask import Flask, request, Response, session
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo , pymongo
from twilio.rest import Client
from dotenv import load_dotenv
from jsonify import convert
import os

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://nikkyvishwa90:nikkyvishwa90@cluster0.jc8u7cz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0/sample_mflix"
# db = PyMongo(app).db
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Sample data to serve
# def endpoint():
# 	results_bulk_iter = iter([])
# 	response = Response(stream_with_context(bulk_update_streamed_response(results_bulk_iter)),
# 					mimetype='text/plain')
# 	return response

# def bulk_update_streamed_response(results):
# 	for updated, _ in results:
# 		yield str(counter).decode('utf-8')
            

client = pymongo.MongoClient('mongodb+srv://shivams:shivams@cluster0.jc8u7cz.mongodb.net/sample_mflix?retryWrites=true&w=majority&appName=Cluster0')
userdb = client['FlaskDB']
users = userdb.users

# Route to get all users
@app.route('/users', methods=['GET', 'POST'])

def get_users():
	return data

@app.route('/insert', methods=['POST', 'GET'])
@cross_origin()
def insert_data():
    
		data = request.get_json()
		# if name != '':
		_id = users.insert_one(data)
		print(_id.inserted_id)
		return 'true'
		# else:
		# 	return "False"

def check_user():

	if request.method == 'POST':
		user = request.get_json()

		user_data = users.find_one(user)
		if user_data == None:
			return False, ""
		else:
			return True, user_data["name"]


# OTP authentication confrigration
account_sid = "ACe153842b9f2450d2a72c5f7386220822"
auth_token = "9f31ad65c96fc712130c192e866192eb"
verify_sid = "VAa978386901f486de36aa578d653eef51"
from_number = "+15706825138"

# account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# verify_sid = os.getenv("VERIFY_SID")
# from_number = os.getenv("TWILIO_NUMBER")
client = Client(account_sid,auth_token)

# # Route to create a new user
@app.route('/create_user', methods=['POST'])
def create_user():
	new_user = request.get_json()
	# if name != '':
	_id = users.insert_one(new_user)
	number = new_user['number']
	send_otp_via_sms(number)
    # data.append(new_user)
	return 'otp send'


def send_otp_via_sms(number):
	# massage = client.messages.create(body="Hello world", from_=from_number,
	#   to=number)
	
	otp_verification = client.verify.services(verify_sid).verifications.create(
	 to=number, channel="sms")
	print(otp_verification.status)
	# print(messages.status['valid'])
	# print(messages.status.valid)
	# print(messages['valid'])
	# print(messages.valid)

    # messages = client.messages.create(to=f"{number}", from_=os.getenv(
    #     'TWILIO_NUMBER'), body=f"Your one-time password is {code}")
# input_otp = input("enter")
# check_opt(input_otp)
@app.route('/check_otp', methods=['POST'])
def check_otp():
	verify_data = request.get_json()
	print(verify_data['number'])
	otp_check = client.verify.services(verify_sid).verification_checks.create(
		to=verify_data['number'], code=verify_data['otp_code']
	)
	print(otp_check.status)
	return 'done'
# Route to get a user by ID
# @app.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = next((u for u in data if u['id'] == user_id), None)
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({'error': 'User not found'}), 404


# # Route to update a user by ID
# @app.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = next((u for u in data if u['id'] == user_id), None)
#     if user:
#         updates = request.get_json()
#         user.update(updates)
#         return jsonify(user)
#     else:
#         return jsonify({'error': 'User not found'}), 404

# # Route to delete a user by ID
# @app.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     global data
#     data = [u for u in data if u['id'] != user_id]
#     return '', 204

if __name__ == '__main__':
    app.run(debug=True)



