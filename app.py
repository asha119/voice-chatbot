from flask import Flask, render_template, request
import random

app = Flask(__name__)

# ---------------------------
# Simple chatbot responses
# ---------------------------
responses = {
    "hi": [
        "Hello! How can I help you today?",
        "Hi there! Nice to see you 😊",
        "Hello! What can I do for you?"
    ],
    "hello": [
        "Hello! How can I assist you?",
        "Hi! Feel free to ask me anything."
    ],
    "who created you": [
        "I was created by Asha Kiran from the CSD department.",
        "I was invented by Asha Kiran as a chatbot project."
    ],
    "what is your purpose": [
        "My purpose is to assist users with friendly and professional responses.",
        "I was created to help and interact with people in a simple way."
    ],
    "hlo": [
        "hi! im here to help you."
    ]
}

# ---------------------------
# Home route
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_input = request.form.get("message", "").lower()

        # Find response
        for key in responses:
            if key in user_input:
                reply = random.choice(responses[key])
                break
        else:
            reply = (
                "Thank you for your question. "
                "I’m here to help — please feel free to ask in a different way."
            )

    return render_template("index.html", reply=reply)

# ---------------------------
# Render-compatible run
# ---------------------------
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
