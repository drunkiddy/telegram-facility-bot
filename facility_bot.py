import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the token you obtained from BotFather
TOKEN = '6963239388:AAHQYANzrN4xOQCyNXfc6wLQp-ub7WjfC2k'

# Define the facility codes you want to monitor
FACILITY_CODES = [
    'CMH1', 'CHO1', 'PHL5', 'ORF2', 'ORF3', 'JFK8', 'LDJ5', 'SYR1', 'SGA1', 'VGA1',
    'LGA5', 'LGA9', 'MKE2', 'AUS2', 'MCI5', 'MSP8', 'MTN1', 'BOS4', 'RFD4', 'MOB5',
    'DET6', 'ABE8', 'ACY2', 'HDT9', 'DTW3', 'DTW9', 'HMK3', 'LIT1', 'FTW1', 'CLT9',
    'GRR1', 'DTW1', 'CLE2', 'EWR4', 'RBD5', 'OWD5', 'OWD9', 'MTN2', 'JAN1', 'VCB3', 'DEN2'
]

# Define the notification message
NOTIFICATION_MESSAGE = "Attention! Facility node {} mentioned in the message."

# Initialize the Telegram bot
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is running!')

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    # Check if any facility code is mentioned in the message
    for code in FACILITY_CODES:
        if re.search(r'\b{}\b'.format(code), text):
            context.bot.send_message(update.effective_chat.id, NOTIFICATION_MESSAGE.format(code))
            # Uncomment the following line to send a photo as a notification
            # context.bot.send_photo(update.effective_chat.id, photo=open('path/to/photo.jpg', 'rb'))

# Add command handlers
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()
