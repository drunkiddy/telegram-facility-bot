from flask import Flask, request
from telegram.ext import Updater, MessageHandler, Filters

app = Flask(__name__)

TOKEN = '6963239388:AAHQYANzrN4xOQCyNXfc6wLQp-ub7WjfC2k'
facility_nodes = set([
    # ... your facility nodes here
])

NOTIFICATION_MESSAGE = 'Facility node detected: {}'

def handle_messages(update, context):
    message_text = update.message.text
    detected_facility_nodes = [node for node in facility_nodes if node in message_text]

    for node in detected_facility_nodes:
        context.bot.send_message(update.message.chat_id, NOTIFICATION_MESSAGE.format(node))

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('UTF-8')
    update = Update.de_json(json_string)
    dp.process_update(update)
    return ''

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, handle_messages))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
