from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# Sample data to serve
data = [
{'id': 1, 'name': 'Shivam gandu', 'age': 30},
{'id': 2, 'name': 'Puneet', 'age': 25},
{'id': 3, 'name': 'Ankit', 'age': 40},
{'id': 4, 'name': 'Akash', 'age': 20},
{'id': 5, 'name': 'Harsit', 'age': 30},
{'id': 6, 'name': 'Vineet', 'age': 25},
]

# client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# userdb = client['userdb']
# users = userdb.customers

# Route to get all users
@app.route('/users', methods=['GET'])
@cross_origin()
def get_users():
    return data

@app.route('/insert', methods=['POST', 'GET'])
def insert_data():
    
	# if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
       
		reg_user = {}
		reg_user['name'] = name
		reg_user['email'] = email
		reg_user['password'] = password
    
		if name != '':
			# users.insert_one(reg_user)
			print('insert - '. reg_user)
			return reg_user
		else:
			return "False"

# Route to get a user by ID
# @app.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = next((u for u in data if u['id'] == user_id), None)
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({'error': 'User not found'}), 404

# # Route to create a new user
# @app.route('/users', methods=['POST'])
# def create_user():
#     new_user = request.get_json()
#     new_user['id'] = len(data) + 1
#     data.append(new_user)
#     return jsonify(new_user), 201

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



