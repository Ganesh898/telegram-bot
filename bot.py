import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 1. Start Command - Isse confirm hoga ki naya code chal raha hai
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bhai, ab code update ho gaya hai! Mujhe koi bhi PDF bhejo, main turant ID de dunga.")

# 2. File ID nikalne wala function
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.document.file_id
    await update.message.reply_text(f"Ye rahi tumhari PDF ki ID:\n\n{file_id}")

def main():
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    # Ye line har document ko pakdegi
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    application.run_polling()

if __name__ == '__main__':
    main()
