import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Aapki Java File ID
JAVA_ID = "BQACAgUAAxkBAANGAuUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAlm1ShWMvWKko0768M2BA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buttons ka design - Code mein aur Button mein text ekdum same hona chahiye
    keyboard = [['Java_chartsheet 📚', 'Physics 🍎'], ['Help 💡']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bhai ab code fix hai! Buttons dabao:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    # Check karte hain ki kaunsa button dabaya gaya
    if text == 'Java_chartsheet 📚':
        await context.bot.send_document(
            chat_id=update.effective_chat.id, 
            document=JAVA_ID, 
            caption="Ye lo bhai Java Cheatsheet! 🔥"
        )
    elif text == 'Help 💡':
        await update.message.reply_text("Buttons pe click karo bhai, notes mil jayenge!")

def main():
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    # Ye line zaroori hai buttons ko read karne ke liye
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
