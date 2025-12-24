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
    elif msg in ["bye","ok","done"]:
        return "ok! thank you for approaching me"
    elif "gyan fest" in msg:
        return "As per college notification 'GYAN-2k25' is conducting on 26th&27th every student participation is mandatory"
    elif "college timings" in msg:
        return "As per college notification college timings are 9:00AM-4:30PM"
    elif "sem exams" in msg:
        return "As per college notification" \
        "31-12-25---Linear Algebra And calculus" \
        "02-01-26---Engineering physics" \
        "05-01-26---Communicative English" \
        "07-01-26---Basic Civil&Mechanical Engineering" \
        "09-01-26---Problem Solving and Programming with C"
    elif "this project" in msg:
        return "The Voice-Enabled AI Chatbot is a web-based application developed to assist students by providing instant answers to academic and administrative queries through both text and voice interaction. The system is designed with a professional and mobile-friendly interface, enabling users to ask questions easily and receive responses in real time. It supports features such as multiple responses for the same question, voice input and output, and dynamic interaction for better user experience. The chatbot allows an admin to update or modify questions and answers at any time, ensuring the information remains accurate and up to date. The project is implemented using HTML, CSS, and JavaScript for the frontend, Python with Flask for backend logic, GitHub for version control, and Render for online hosting and accessibility. Overall, the chatbot improves accessibility to information, saves time for students, and provides an efficient digital solution for handling common college-related queries."
    
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
