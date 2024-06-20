from typing  import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes

TOKEN:Final ='7405232209:AAE-qvH6YUbfi5qkLWJu8rAcsRjs2du9B-s'
BOT_USERNAME: Final='@Banana_fruit_bot'


# commands are below
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to Banana Fruits world!!!')
async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am banana bot, please type query for the response')
async def custom_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

# response of bot

def handle_response(text:str)-> str:

    processed: str=text.lower()

    if 'hello' in processed:
        return 'Hey there'
    
    if 'how are you' in processed:
        return 'I\'m delicious'
    
    if 'python' in processed:
        return 'use this bot, wisely...'
    
    return 'I don\'t understand your query... try again'

# to user

async def handle_msg(update: Update,context:ContextTypes.DEFAULT_TYPE):
    msg_type:str =update.message.chat.type
    text:str=update.message.text

    print(f"user ({update.message.chat.id}) in {msg_type} : '{text}'")

    if msg_type == 'group':
        if BOT_USERNAME in text:
            new_txt: str=text.replace(BOT_USERNAME,'').strip()
            response: str=handle_response(new_txt)
        else:
            return
    else: 
        response: str=handle_response(text=text)
    
    print('Bot: ',response)
    await update.message.reply_text(response)


async def error(update: Update,context:ContextTypes.DEFAULT_TYPE):
    print(f"update: {update} caused error: {context.error}")


if __name__=='__main__':
    print('starting the bot')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    #messages

    app.add_handler(MessageHandler(filters.TEXT,handle_msg))

    # Error
    app.add_error_handler(error)
    print('polling...')

    app.run_polling(poll_interval=3)