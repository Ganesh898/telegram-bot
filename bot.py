import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- YAHAN APNI FILE IDs DALO ---
JAVA_CHEATSHEET_PDF = "BQACAgUAAxkBAANGaUUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAIm1ShWMvWKko0768M2BA"
JAVA_PDF = "BQACAgUAAxkBAANGaUUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAIm1ShWMvWKko0768M2BA"
PHYSICS_PDF = "PASTE_YOUR_PHYSICS_ID_HERE"

# 1. Start Command (Buttons ke saath)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buttons ka design
    keyboard = [['Java_chartsheet 📚', 'Physics 🍎'], ['Help 💡']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Welcome bhai! Konsa notes chahiye? Niche buttons use karo:",
        reply_markup=reply_markup
    )

# 2. Buttons click hone par kya hoga
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == 'java 😈':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=JAVA_CHEATSHEET_PDF, caption="Ye lo java cheatsheet ke notes! 🔥")
    
    elif text == 'Physics 🍎':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=PHYSICS_PDF, caption="Ye lo Physics ke notes! 🚀")
    
    elif text == 'Help 💡':
        await update.message.reply_text("Bhai simple hai, buttons pe click karo notes mil jayenge!")

def main():
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()

