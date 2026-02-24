from flask import Flask, render_template, request, jsonify
import datetime

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
        except:
            return "Hmm, I couldn't calculate that."
    elif "how are you" in message:
        return "I'm just code, but I'm doing great!"
    else:
        return "Sorry, I don't understand that yet."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]
    response = giznos_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
