import telebot
import csv
import datetime

TOKEN = "8581202055:AAF4YtVSapZRFGbqc9mMp3ml9Y_eRZX-vbk"
bot = telebot.TeleBot(TOKEN)

try:
    with open('bot_logs.csv', 'x', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'user', 'message'])
except FileExistsError:
    pass 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hej, jag är en enkel Telegram-bot.\nKommandon:\nstart - börja\n/csv - skapa CSV fil\n/help - hjälp")

@bot.message_handler(commands=['help'])
def help(message):
    log_message(message, '/help')
    bot.reply_to(message, "jag kan:\n1 säga Hej\n2. Skapa CSV filer\n3. Repetera din a meddelanden")

@bot.message_handler(commands=['csv'])
def create_csv(message):
    log_message(message, '/csv')

    with open('data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Namn', 'Ålder', 'Stad'])
        writer.writerow(['Anna', '25', 'Stockholm'])
        writer.writerow(['Erik', '30', 'Göteborg'])

    with open('data.csv', 'rb') as f:
        bot.send_document(message.chat.id, f, caption="Här är din CSV fil!")
        bot.reply_to(message, "CVs fil skapad")


@bot.message_handler(func=lambda message: True)
def echo(message):
    log_message(message, message.text)
    bot.reply_to(message, f"du skrev: {message.text}")

def log_message(message, text):
    with open('bot_logs.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.datetime.now(). strftime('%Y-%m-%d %H:%M:%S'),
            message.from_user.username or message.from_user.id,
            text
        ])

print("Boten är idång")
print("Skapar CSV-filer...")
bot.polling()