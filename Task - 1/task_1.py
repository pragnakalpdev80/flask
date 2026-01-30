from flask import Flask,jsonify,request,json
import uuid
import json

app=Flask(__name__)

def check_uuid(user_id):
    try:
        uuid.UUID(user_id)
    except ValueError:
        return False
    return True

def load_users():
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
            users = data.get("users")
            return users
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False    
 
def write_users(users):
    with open("users.json", "w") as f:
        updated_users={"users":users}
        json.dump(updated_users,f,indent=4)   
     
@app.route("/users",methods=['POST'])
def create_users():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400
    if 'email' not in data:
        return jsonify({"error": "Missing 'email' field"}), 400
    if 'age' not in data:
        return jsonify({"error": "Missing 'age' field"}), 400
    if not isinstance(data.get('age'), int):
        return jsonify({"error": "Age must be an integer"}), 400
    
    users=load_users()
    if not users:
        return jsonify({"error":"interal server error"}),500
    
    new_user={
        "id":str(uuid.uuid4()),
        "name":data['name'],
        "email":data['email'],
        "age":data['age']
    }
    users.append(new_user)
    write_users(users)
    return jsonify({"message":"User created successfully","user":new_user}), 201

@app.route("/users",methods=['GET'])
def get_all_users():
    users=load_users()
    if not users:
        return jsonify({"error":"interal server error"}),500
     
    return jsonify(users), 200

@app.route("/users/<user_id>",methods=['GET'])
def get_user(user_id):

    if not check_uuid(user_id):
        return jsonify({"error": "Invalid UUID format"}), 500
    
    users=load_users()
    if not users:
        return jsonify({"error":"interal server error"}),500
    
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200

@app.route("/users/<user_id>",methods=['PATCH'])
def update_users(user_id):

    if not check_uuid(user_id):
        return jsonify({"error": "Invalid UUID format"}), 400
    
    users=load_users()
    if not users:
        return jsonify({"error":"interal server error"}),500
    
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    users.remove(user)
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    if 'name' in data:
        user['name']=data['name']
    if 'email' in data:
        user['email']=data['email']
    if 'age' in data:
        if (type(data.get('age'))!=int):
            return jsonify({"error": "Age must be an integer"}), 400
        user['age']=data['age']
    users.append(user)
    write_users(users)
    return jsonify({"message":"User updated successfully","user":user}), 200

@app.route("/users/<user_id>",methods=['DELETE'])
def delete_user(user_id):

    if not check_uuid(user_id):
        return jsonify({"error": "Invalid UUID format"}), 400
    
    users=load_users()
    if not users:
        return jsonify({"error":"interal server error"}),500
    
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    users.remove(user)
    write_users(users)
    return jsonify({"message":"User deleted successfully"}), 200

if __name__=="__main__":
    app.run(debug=True)