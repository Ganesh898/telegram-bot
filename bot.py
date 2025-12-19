import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ID yahan fixed hai
JAVA_ID = "BQACAgUAAxkBAANGAuUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAlm1ShWMvWKko0768M2BA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['Java_chartsheet 📚', 'Physics 🍎'], ['Help 💡']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bhai code fixed hai! Buttons use karo:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == 'Java_chartsheet 📚':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=JAVA_ID, caption="Ye lo Java notes!")
    elif text == 'Help 💡':
        await update.message.reply_text("Buttons pe click karo bhai!")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        return # Token nahi mila toh band ho jaye
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
