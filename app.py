from flask import Flask, render_template, request, jsonify
from rag import retrieve_answer

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Chat API
@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    user_message = data["message"]

    answer = retrieve_answer(user_message)

    return jsonify({"reply": answer})


if __name__ == "__main__":
    app.run(debug=True)