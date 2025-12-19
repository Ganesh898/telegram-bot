import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# --- Yahan apni Admin ID daalo ---
ADMIN_ID = 2104563445 

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Check karega ki bhejnewala sirf aap ho ya nahi
    if user_id == ADMIN_ID:
        # Check files: Document, Video, Photo, ya Audio
        if update.message.document:
            file_id = update.message.document.file_id
            file_type = "Document"
        elif update.message.video:
            file_id = update.message.video.file_id
            file_type = "Video"
        elif update.message.photo:
            file_id = update.message.photo[-1].file_id # Sabse high quality photo
            file_type = "Photo"
        elif update.message.audio:
            file_id = update.message.audio.file_id
            file_type = "Audio"
        else:
            return

        # Aapko sundar format mein ID bhejega
        response = (
            f"✅ **{file_type} ki ID mil gayi!**\n\n"
            f"`{file_id}`\n\n"
            f"👆 Isse copy karke apne main bot mein use karlo."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
    else:
        # Agar koi aur file bhejta hai toh bot ignore karega
        pass

def main():
    # Apna naya Bot Token yahan environment variable mein set karein
    token = os.getenv("ID_BOT_TOKEN") 
    
    if not token:
        print("Error: ID_BOT_TOKEN nahi mila!")
        return

    application = Application.builder().token(token).build()

    # Ye handler har tarah ki files (Document, Video, Photo) ko detect karega
    application.add_handler(MessageHandler(filters.ATTACHMENT, get_file_id))

    print("ID Generator Bot chalu ho gaya hai...")
    application.run_polling()

if __name__ == '__main__':
    main()
    
