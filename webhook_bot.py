from flask import Flask, request
import telegram
import os

TOKEN = "7613420464:AAEHh5Uo5YgH0PEN_J8s5H1_UU21WOFbL1c"
CHAT_ID = "<YOUR_CHAT_ID>"  # Replace this with your actual chat ID

bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "SnipeFVG Bot is Live!"

@app.route('/snipefvgwebhook123', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if "message" in data:
        print("Received message from user.")
    
    bot.send_message(chat_id=CHAT_ID, text="🚀 New FVG Signal on EUR/USD (1-Min)\nCheck the chart on Forex.com now!")
    
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, port=5000)