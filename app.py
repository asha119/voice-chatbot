from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def chatbot_response(user_msg):
    msg = user_msg.lower()

    if "who created you" in msg or "who invented you" in msg:
        return "I was invented by Asha Kiran from the CSD department."
    elif "purpose" in msg:
        return "My purpose is to assist users in a friendly and professional manner."
    elif msg in ["hi", "hello", "hlo", "hey"]:
        return "Hello! How can I help you today?"
    else:
        return "Thank you for your message. I am still learning and will improve over time."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = chatbot_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
