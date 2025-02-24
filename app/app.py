from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify(result=a + b)

@app.route('/subtract')
def subtract():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify(result=a - b)

@app.route('/multiply')
def multiply():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify(result=a * b)

@app.route('/divide')
def divide():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if b == 0:
        return jsonify(error="Division by zero is not allowed"), 400
    return jsonify(result=a / b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)