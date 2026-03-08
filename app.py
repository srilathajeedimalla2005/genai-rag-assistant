from flask import Flask, send_from_directory, request, jsonify
from rag import retrieve_answer

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/styles.css")
def style():
    return send_from_directory(".", "styles.css")

@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    user_message = data["message"]

    answer = retrieve_answer(user_message)

    return jsonify({"reply": answer})


if __name__ == "__main__":
    app.run(debug=True)