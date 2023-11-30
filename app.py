import pyrebase
from flask import Flask, request, jsonify, render_template
from rasa.core.agent import Agent
from flask_cors import CORS

config = {
    "apiKey": "AIzaSyAhnX2Yc09kQjeiuSTFQW_rd796RF7vUPc",
    "authDomain": "tamilspeakingaigirlfriend.firebaseapp.com",
    "databaseURL": "https://tamilspeakingaigirlfriend-default-rtdb.firebaseio.com",
    "projectId": "tamilspeakingaigirlfriend",
    "storageBucket": "tamilspeakingaigirlfriend.appspot.com",
    "messagingSenderId": "820736637033",
    "appId": "1:820736637033:web:4a2042f9c336c5cafecaf8",
    "measurementId": "G-8H1E29GJVC"
}
firebase = pyrebase.initialize_app(config)

app = Flask(__name__, static_folder= "templates")
CORS(app)
# Load Rasa model
agent = Agent.load("./models")

@app.route("/signin")
def signin():
    pass

@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json()
    user_message = data["message"]

    # Get Rasa response
    bot_reply = await agent.handle_text(user_message)

    # Extract the bot's reply

    return jsonify({"message": bot_reply})

@app.route("/home", methods=["GET"])
def home():
    return render_template('chatui.html')

if __name__ == "__main__":
    app.run(debug=True)
