from flask import Flask, request, jsonify, render_template
from rasa.core.agent import Agent
from flask_cors import CORS

app = Flask(__name__, static_folder= "templates")
CORS(app)
# Load Rasa model
agent = Agent.load("C:\\Users\\Kanujan\\Desktop\\Kanujan\\Projects\\aigi\\my-models")

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
