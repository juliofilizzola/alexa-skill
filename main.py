from flask import Flask, request, jsonify
from skills.pc import handle_intent

app = Flask(__name__)

@app.route('/alexa', methods=['POST'])
def alexa_endpoint():
    data = request.get_json()
    intent = data['request']['intent']['name']

    response = handle_intent(intent)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)