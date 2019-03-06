import os
import sys
import traceback

import tasks
from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)


def start(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id = chat_id, text = "threepwood Bot")
    
def echo(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    
    task_cls_list = {
        tasks.HelloTask,
        tasks.NaverBlogSearchTask
    }
    
    try:
        for task_cls in task_cls_list:
            task = task_cls(text)
            if task.is_valid():
                response = task.proc()
                break
            else:
                response = "What?"
    except Exception as e:
        response = "error"
        traceback.print_exc()

    bot.send_message(chat_id = chat_id, text = response)
    
def main(token):
    bot = Updater(token = TOKEN)
    
    handler = CommandHandler('start', start)
    bot.dispatcher.add_handler(handler)
    
    handler = MessageHandler(Filters.text, echo)
    bot.dispatcher.add_handler(handler)
    
    bot.start_polling()
    
    print('start')
    bot.idle()
    
if __name__ == '__main':
    TOKEN = '770602880:AAGQsuy3uK-H5YCHqARjPKJnsmIIddwZ8TY'
    if TOKEN is None :
        print('token error')
        sys.exit(1)
    main(TOKEN)
