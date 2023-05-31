from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'text': 'Hello!'})

@app.route('/app/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({'error': 'Both num1 and num2 must be provided'}), 400

    try:
        result = int(num1) + int(num2)
    except ValueError:
        return jsonify({'error': 'Both num1 and num2 must be integers'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)