import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bhai, tension mat lo! Ab mujhe koi PDF bhejo, main uski ID bata dunga.")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.document.file_id
    await update.message.reply_text(f"ID mil gayi bhai! Ye rahi:\n\n{file_id}")

def main():
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.run_polling()

if __name__ == '__main__':
    main()
