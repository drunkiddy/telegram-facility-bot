from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with the actual token provided by BotFather
TOKEN = '6963239388:AAHQYANzrN4xOQCyNXfc6wLQp-ub7WjfC2k'

# Facility codes
facility_nodes = set([
    "CMH1", "CHO1", "PHL5", "ORF2", "ORF3", "JFK8", "LDJ5", "SYR1", "SGA1",
    "VGA1", "LGA5", "LGA9", "MKE2", "AUS2", "MCI5", "MSP8", "MTN1", "BOS4",
    "RFD4", "MOB5", "DET6", "ABE8", "ACY2", "HDT9", "DTW3", "DTW9", "HMK3",
    "LIT1", "FTW1", "CLT9", "GRR1", "DTW1", "CLE2", "EWR4", "RBD5", "OWD5",
    "OWD9", "MTN2", "JAN1", "VCB3", "DEN2"
])

# Replace 'YOUR_MESSAGE' with the notification message you want to send
NOTIFICATION_MESSAGE = 'Facility node detected: {}'

def start(update, context):
    update.message.reply_text('Hello! I am your facility bot. Mention a facility node to receive a notification.')

def handle_messages(update, context):
    message_text = update.message.text
    detected_facility_nodes = [node for node in facility_nodes if node in message_text]

    for node in detected_facility_nodes:
        context.bot.send_message(update.message.chat_id, NOTIFICATION_MESSAGE.format(node))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, handle_messages))
    dp.add_handler(MessageHandler(Filters.COMMAND, start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
