from flask import Flask, request, jsonify
from stbbot import construct_index, ask_ai
from gpt_index import GPTSimpleVectorIndex
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/stbbot": {"origins": "*"}})
index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route("/stbbot", methods=["POST"])

def stbbot():
    user_msg = request.json['user_msg']
    print(f'Received user message: {user_msg}')
    botResponse = ask_ai(user_msg)
    print(f'Sending bot response: {botResponse}')
    response = {'bot_response: ': botResponse}
    return jsonify({'bot_response: ': botResponse})

if __name__ == "__main__":
    app.run(debug=True)