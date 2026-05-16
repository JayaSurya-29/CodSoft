from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random
import re

app = Flask(__name__)

@app.errorhandler(500)
def internal_error(error):
    return f"Internal Server Error: {error}", 500

def chatbot_response(message):
    msg = message.lower()
    
    greetings = [
        "Hello 👋 Welcome to SmartBot!",
        "Hi there 😊 How can I assist you?",
        "Hey! Great to see you! 🚀",
        "Hi! What's on your mind today?"
    ]
    
    jokes = [
        "Why do programmers hate nature? Too many bugs 😂",
        "Python developers don't bite, they hiss 🐍",
        "Why did Python go to school? To improve its class 😆",
        "What's a programmer's favorite type of coffee? Java! ☕",
        "Why don't programmers like sunlight? It causes glares! 🌞"
    ]
    
    motivation = [
        "Believe in yourself 💪 You're amazing!",
        "Success comes from consistency 🚀 Keep going!",
        "Keep learning and growing 📚",
        "You're capable of incredible things! ✨",
        "Every day is a new chance to improve!"
    ]
    
    how_are_you = [
        "I'm doing great 😎 Thanks for asking!",
        "Feeling fantastic! ✨ How about you?",
        "Wonderful! Ready to help! 🌟"
    ]
    
    bye = [
        "Goodbye 👋 Have a wonderful day!",
        "See you later! 👋 Take care!",
        "Bye! Come back anytime! 👋"
    ]
    
    thanks = [
        "You're welcome! 😊",
        "Happy to help! ✨",
        "Anytime! 🌟"
    ]
    
    what_can_you_do = [
        "I can help with time, date, math, jokes, motivation, and small talk! 😊",
        "Try asking about time, date, math problems, or tell me you need a joke!"
    ]
    
    small_talk = [
        "That's interesting! Tell me more 😊",
        "Cool! What else is on your mind?",
        "Nice! How's your day going?"
    ]
    
    if any(word in msg for word in ["hi", "hello", "hey", "hola"]):
        return random.choice(greetings)
    
    elif "your name" in msg:
        return "I am SmartBot 🤖 Your friendly chat assistant!"
    
    elif "time" in msg:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"⏰ Current time is {current_time}"
    
    elif "date" in msg:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"📅 Today's date is {current_date}"
    
    elif "how are you" in msg:
        return random.choice(how_are_you)
    
    elif any(word in msg for word in ["joke", "funny", "laugh"]):
        return random.choice(jokes)
    
    elif any(word in msg for word in ["motivate", "inspire", "encourage"]):
        return random.choice(motivation)
    
    elif any(word in msg for word in ["help", "what can you do", "capabilities"]):
        return random.choice(what_can_you_do)
    
    elif any(word in msg for word in ["bye", "goodbye", "see you"]):
        return random.choice(bye)
    
    elif any(word in msg for word in ["thank", "thanks", "thx"]):
        return random.choice(thanks)
    
    elif re.search(r'\d+\s*[+\-*/]\s*\d+', msg):
        try:
            result = eval(re.search(r'\d+\s*[+\-*/]\s*\d+', msg).group())
            return f"🧮 The result is {result}!"
        except:
            return "🤔 Hmm, I couldn't calculate that. Try a simple math problem like 2+2!"
    
    elif any(word in msg for word in ["you're smart", "you're cool", "great", "awesome"]):
        return "Aww, thanks! You're pretty awesome too! 😊"
    
    elif "what is" in msg or "what's" in msg:
        return "I'm a rule-based chatbot, but I can help with time, date, math, and more! 😊"
    
    else:
        return random.choice(small_talk) + " Or ask me about time, date, math, jokes, or motivation!"

@app.route("/", methods=["GET", "HEAD"])
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_message = request.form["message"]
    response = chatbot_response(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=False)
