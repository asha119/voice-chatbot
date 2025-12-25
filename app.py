from flask import Flask, render_template, request, jsonify
import random
import openai

app = Flask(__name__)

# -------------------------
# OPENAI API KEY (TEMP)
# -------------------------
openai.api_key = "PASTE_YOUR_API_KEY_HERE"

# -------------------------
# Predefined Q&A (Hybrid)
# -------------------------
qa_data = {
    "hi": ["Hello! How can I help you today? 😊"],
    "who created you": ["I was created by Asha Kiran from the CSD Department."],
    "what is your purpose": ["My purpose is to assist students with instant information."],
}

# -------------------------
# Home Route
# -------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_msg = request.form.get("message", "").lower()

        # 1️⃣ Check predefined answers first
        for q in qa_data:
            if q in user_msg:
                return jsonify({"reply": random.choice(qa_data[q])})

        # 2️⃣ Else → Use AI API
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful student assistant."},
                    {"role": "user", "content": user_msg}
                ],
                max_tokens=150
            )

            ai_reply = response.choices[0].message["content"]
            return jsonify({"reply": ai_reply})

        except Exception as e:
            return jsonify({"reply": "AI service is temporarily unavailable."})

    return render_template("index.html")


# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
