import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 1. Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bhai, ab mujhe koi PDF bhejo, main uski ID dunga!")

# 2. File ID nikalne wala function
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # PDF ke liye
    if update.message.document:
        file_id = update.message.document.file_id
        await update.message.reply_text(f"PDF ID mil gayi:\n\n{file_id}")
    # Video ke liye
    elif update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"Video ID mil gayi:\n\n{file_id}")

def main():
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    # Ye line PDF aur Video dono detect karegi
    application.add_handler(MessageHandler(filters.Document.ALL | filters.VIDEO, handle_document))

    application.run_polling()

if __name__ == '__main__':
    main()
