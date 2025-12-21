from flask import Flask, render_template, request, session
from flask_session import Session
import string
import random

app = Flask(__name__)

# ----------------- CONFIG -----------------
app.secret_key = "chatbot_secret_key"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# ------------------------------------------

# ----------- CUSTOM QUESTIONS & ANSWERS -----------
custom_qa = {
    # ---- GREETINGS ----
    "hi": [
        "Hello! 👋 How can I assist you today?",
        "Hi there! 😊 How may I help you?",
        "Welcome! 👋 What can I do for you?"
    ],
    "hlo": [
        "Hello! 👋 How can I assist you today?",
        "Hi! 😊 How may I help you?"
    ],
    "hello": [
        "Hello! 👋 How can I assist you today?",
        "Hi there! 😊 How may I help you?",
        "Greetings! 👋 What can I do for you?"
    ],
    "hey": [
        "Hey! 😊 How can I help you?",
        "Hello! 👋 What would you like to know?"
    ],

    # ---- BASIC QUESTIONS ----
    "how are you": [
        "I’m doing well, thank you for asking! 😊",
        "I’m functioning perfectly and ready to help! 🤖",
        "All good here! How can I assist you?"
    ],

    "who created you": [
        "I was created by Asha Kiran from the CSD Department.",
        "This chatbot was developed by Asha Kiran (CSD Department).",
        "I was proudly designed by Asha Kiran from the CSD Department."
    ],

    "purpose of inventing you": [
        "I was created to demonstrate a professional chatbot project.",
        "My purpose is to assist users and showcase chatbot development.",
        "I was developed as a professional academic chatbot project."
    ],

    "bye": [
        "Goodbye! Have a great day ahead. 😊",
        "Thank you for chatting. Take care!",
        "See you soon! 👋"
    ],

    "banu evaru": [
        "he is a bad boy"
    ]

}


# --------------------------------------------------


def clean_text(text):
    """Normalize user input"""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(text.split())
    return text


def get_reply(user_message):
    msg = clean_text(user_message)

    # Match custom questions
    for question, answers in custom_qa.items():
        if question in msg:
            return random.choice(answers)

    # Professional fallback responses
    fallback_responses = [
        "I’m continuously learning and may not have an answer to that at the moment.",
        "That is an interesting question. I’ll continue learning to assist you better.",
        "I do not have information on that right now, but I’m here to help with other questions."
    ]
    return random.choice(fallback_responses)


# ---------------- HOME ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def home():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_msg = request.form["message"]
        bot_reply = get_reply(user_msg)

        session["chat_history"].append({
            "type": "user",
            "message": user_msg
        })
        session["chat_history"].append({
            "type": "bot",
            "message": bot_reply
        })

    return render_template("index.html", chat_history=session["chat_history"])
# ------------------------------------------------


# -------- CLEAR CHAT WHEN TAB IS CLOSED --------
@app.route("/clear", methods=["POST"])
def clear_chat():
    session.pop("chat_history", None)
    return "", 204
# ------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)

