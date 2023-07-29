import os
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, CallbackContext
from document_chat import retrieval_chat
load_dotenv()

qa = retrieval_chat()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def generate_answer(user_message):
    return qa.answer_question(user_message)

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text  # Extract the user's message
    response = generate_answer(user_message)  # Generate a response
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)  # Send the response

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_KEY")).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    application.add_handler(start_handler)
    application.add_handler(message_handler)

    application.run_polling()