import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# 1. Yahan apni Admin ID daalo
ADMIN_ID = 2104563445 

# Logging setup (taaki error aaye toh terminal pe dikhe)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def get_id_logic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Sirf aapko reply karega
    if update.effective_user.id != ADMIN_ID:
        return

    file_id = None
    
    # Har tarah ki file check karega
    if update.message.document:
        file_id = update.message.document.file_id
    elif update.message.video:
        file_id = update.message.video.file_id
    elif update.message.photo:
        file_id = update.message.photo[-1].file_id
    elif update.message.audio:
        file_id = update.message.audio.file_id

    if file_id:
        await update.message.reply_text(f"✅ **ID Mil Gayi:**\n\n`{file_id}`", parse_mode='Markdown')

def main():
    # 2. Yahan apna Naya Bot Token dalo
    TOKEN = "import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# 1. Yahan apni Admin ID daalo
ADMIN_ID = 2104563445 

# Logging setup (taaki error aaye toh terminal pe dikhe)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def get_id_logic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Sirf aapko reply karega
    if update.effective_user.id != ADMIN_ID:
        return

    file_id = None
    
    # Har tarah ki file check karega
    if update.message.document:
        file_id = update.message.document.file_id
    elif update.message.video:
        file_id = update.message.video.file_id
    elif update.message.photo:
        file_id = update.message.photo[-1].file_id
    elif update.message.audio:
        file_id = update.message.audio.file_id

    if file_id:
        await update.message.reply_text(f"✅ **ID Mil Gayi:**\n\n`{file_id}`", parse_mode='Markdown')

def main():
    # 2. Yahan apna Naya Bot Token dalo
    TOKEN = "8275861375:AAFJnfntOp1zVTiHwFMrDYxDqiDUsfsSeuk" # <--- Apna token yahan paste karo

    # Application build
    app = Application.builder().token(TOKEN).build()

    # Filter ko 'ALL' rakha hai taaki kuch bhi miss na ho
    app.add_handler(MessageHandler(filters.ALL, get_id_logic))

    print("Bot chalu hai... File bhejo!")
    app.run_polling()

if __name__ == '__main__':
    main()
 # <--- Apna token yahan paste karo

    # Application build
    app = Application.builder().token(TOKEN).build()

    # Filter ko 'ALL' rakha hai taaki kuch bhi miss na ho
    app.add_handler(MessageHandler(filters.ALL, get_id_logic))

    print("Bot chalu hai... File bhejo!")
    app.run_polling()

if __name__ == '__main__':
    main()
    
