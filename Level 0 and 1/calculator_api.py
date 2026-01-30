from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route("/calculate", methods=['POST'])
def calculator():
    data = request.get_json()

    if not data or 'operation' not in data:
        return jsonify({"error": "Missing operation"}), 400

    
    operation = data['operation']
    x = data.get('x', 0)
    y = data.get('y', 0)

    if not (type(x)==int or type(x)==float):
        return jsonify({"error": "'x' must be int or float"}), 400
    if not (type(y)==int or type(y)==float):

        return jsonify({"error": "'y' must be int or float"}), 400
    
    if operation == 'add':
        result = x + y
    elif operation == 'subtract':
        result = x - y
    elif operation == 'multiply':
        result = x * y
    elif operation == 'divide':
        if y == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = x / y
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result}), 200


if __name__=="__main__":
    app.run(debug=True)