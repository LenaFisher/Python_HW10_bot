from ast import operator
from telegram import Update
import datetime
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



def log(update: Update, context: ContextTypes.DEFAULT_TYPE, res: str):
    file = open("db.csv", "a")
    file.write(f"{datetime.datetime.now()}, {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {res}\n")
    file.close()