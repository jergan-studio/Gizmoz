from flask import Flask, render_template, request, jsonify
import datetime
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

def giznos_response(message):
    message = message.lower()
    
    if "hello" in message or "hi" in message:
        return "Hello there!"
    elif "time" in message:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}"
    elif any(op in message for op in ["+", "-", "*", "/"]):
        try:
            return f"The answer is {eval(message)}"
        except Exception as e:
            logging.error(f"Math error: {e}")
            return "Hmm, I couldn't calculate that."
    elif "how are you" in message:
        return "I'm just code, but I'm doing great!"
    else:
        return "Sorry, I don't understand that yet."

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        logging.error(f"Template error: {e}")
        return "Error loading page."

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_message = request.form.get("message", "")
        response = giznos_response(user_message)
        return jsonify({"response": response})
    except Exception as e:
        logging.error(f"Ask error: {e}")
        return jsonify({"response": "Oops, something went wrong."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logging.info(f"Starting Giznos on port {port}")
    app.run(host="0.0.0.0", port=port)
