from flask import Flask
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

# Route to get all users
@app.route('/users', methods=['GET'])
@cross_origin()
def get_users():
    return jsonify({"code": 200, "message": "Signup success", "data": info})



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



