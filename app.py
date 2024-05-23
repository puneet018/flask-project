from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo , pymongo

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
            
data = [
{'id': 1, 'name': 'Shivam', 'age': 30},
{'id': 2, 'name': 'Puneet', 'age': 25},
{'id': 3, 'name': 'Ankit', 'age': 40},
{'id': 4, 'name': 'Akash', 'age': 20},
{'id': 5, 'name': 'Harsit', 'age': 30},
{'id': 6, 'name': 'Vineet', 'age': 25},
]

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
    
	# if request.method == 'POST':
		data = request.get_json()
		# name = request.form['name']
		# email = request.form['email']
		# password = request.form['password']
       
		# reg_user = {}
		# reg_user['name'] = name
		# reg_user['email'] = email
		# reg_user['password'] = password
    
        # parser = reqparse.RequestParser()
        # parser.add_argument('title', required=True)
        # parser.add_argument('author', required=True)
        # parser.add_argument('published_date', required=True)
        #     args = parser.parse_args()

		# if name != '':
		_id = users.insert_one(data)
		print(_id.inserted_id)
		return 'true'
		# else:
		# 	return "False"

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



