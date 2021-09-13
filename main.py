import requests
from telegram.ext import *
import json


url = "https://free-football-soccer-videos.p.rapidapi.com/"
API_KEY = '1987298688:AAEllrHTj8YmHX7AXSwKaN_AKr8mlG1Rel4'
headers = {
    'x-rapidapi-host': "free-football-soccer-videos.p.rapidapi.com",
    'x-rapidapi-key': "becd31ca73msha66b98fc2e2a9c8p11530djsnaa4903a5da47"
    }

response = requests.request("GET", url, headers=headers).json()

def start_command(update, context):
    update.message.reply_text("""Klubun adını yazın
    """)
    
    
def club(club):
    
    for i in response:
        for j, value in i.items():
            if 'vs' in value and club in value:
                return value
           

def handle_message(update, context):
    text = update.message.text
    text = text.lower()
    response = club(text)
    update.message.reply_text(response)

def main():
    updater = Updater(API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    # dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.bot.setWebhook('https://boiling-wildwood-00579.herokuapp.com/' + API_KEY)
    updater.start_polling(1)
    updater.idle()
if __name__ == '__main__':
    main()

