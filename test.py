from telegram.ext._updater import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram.ext.filters import BaseFilter

updater = Updater("6322178686:AAFKrFLXiSMk6KYZ8cIDZdqZ4UyNapjgdSM", use_context=True)

def start(update:Update,context:CallbackContext):
    update.message.reply_text("you did it yoni")


updater.dispatcher.add_handler(CommandHandler('start', start))

print('[SERVER RUNING ....]')

updater.start_polling()