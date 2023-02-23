from flask import Flask, request, jsonify
from stbbot import construct_index, ask_ai
from gpt_index import GPTSimpleVectorIndex

app = Flask(__name__)

index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route("/stbbot", methods=["POST", "GET"])
def sbtbot():
    user_msg = request.form['user_msg']

    botResponse = ask_ai(user_msg)

    response = {'bot_response: ': botResponse}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)