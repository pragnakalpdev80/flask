from flask import Flask, request, jsonify
from services.calculation_service import CalculationService

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    # Validation
    if not data:
        return jsonify({"error": "Request body required"}), 400

    operation = data.get("operation")
    x = data.get("x")
    y = data.get("y")

    if not all([operation, x is not None, y is not None]):
        return jsonify({"error": "Missing operation, x, or y"}), 400

    # Call the service
    try:
        result = CalculationService.calculate(operation, x, y)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
if __name__=="__main__":
    app.run(debug=True)