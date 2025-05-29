from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler

TOKEN: Final = "<YOUR BOT ACCESS TOKEN>"
BOT_USERNAME: Final = "@<YOUR BOT USERNAME>"

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!, I am here to help you")

async def help_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am there to help you, type something so i can respond")

async def custom_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")


def handle_responses(text:str)-> str:
    text: str = text.lower()


    if 'hello' in text:
        return "hello there!"
    
    if "how are you" in text:
        return "I am a bot, i always have electrifying energy !"
    
    if "i love python" in text:
        return "I love too!"
    
    else:
        return "Sorry ! , I can't decode that"
    

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type
    text : str = update.message.text

    print(f'user : {update.message.chat.id} in {message_type} : "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, " ").strip()
            response: str = handle_responses(new_text)

        else:
            return
    else:
        response: str = handle_responses(text)

    print("Bot" , response)
    await update.message.reply_text(response)


async def error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    print("Starting...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval = 3)
