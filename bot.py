import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# --- Yahan apni Admin ID daalo ---
ADMIN_ID = 2104563445 

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Sirf admin check
    if update.effective_user.id != ADMIN_ID:
        return

    # File detect logic
    file_id = None
    file_type = ""

    if update.message.document:
        file_id = update.message.document.file_id
        file_type = "Document"
    elif update.message.video:
        file_id = update.message.video.file_id
        file_type = "Video"
    elif update.message.photo:
        file_id = update.message.photo[-1].file_id
        file_type = "Photo"
    elif update.message.audio:
        file_id = update.message.audio.file_id
        file_type = "Audio"

    if file_id:
        await update.message.reply_text(
            f"✅ **{file_type} ID mil gayi!**\n\n`{file_id}`",
            parse_mode='Markdown'
        )

def main():
    # Is bot ke liye ek naya TOKEN use karein (BotFather se le kar)
    token = "YAHAN_APNA_NEW_BOT_TOKEN_DAALO" 
    
    if not token or token == "YAHAN_APNA_NEW_BOT_TOKEN_DAALO":
        print("Error: Please provide a valid Bot Token!")
        return

    application = Application.builder().token(token).build()

    # Filters.ALL se ye har tarah ki file pakad lega
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, get_file_id))

    print("ID Generator Bot ready hai... File bhejo bhai!")
    application.run_polling()

if __name__ == '__main__':
    main()
    
