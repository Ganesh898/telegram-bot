async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Yahan dhyan do: Text ekdum wahi hona chahiye jo button pe likha hai
    if text == 'Java_chartsheet 📚':
        await context.bot.send_document(
            chat_id=update.effective_chat.id, 
            document="BQACAgUAAxkBAANGAuUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAlm1ShWMvWKko0768M2BA", 
            caption="Ye lo bhai Java Cheatsheet! 🔥"
        )
    
    elif text == 'Physics 🍎':
        # Yahan Physics ki ID daal dena
        await context.bot.send_document(
            chat_id=update.effective_chat.id, 
            document="PASTE_PHYSICS_ID_HERE", 
            caption="Ye lo Physics ke notes! 🚀"
        )
