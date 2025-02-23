from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a + b
        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide two numbers."}), 400

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a - b
        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide two numbers."}), 400

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a * b
        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide two numbers."}), 400

@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed."}), 400
        result = a / b
        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide two numbers."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)