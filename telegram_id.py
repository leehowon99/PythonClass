import os
import sys
sys.path.insert(0, 'E:\Python\Lib\site-packages\python_telegram_bot-11.1.0.dist-info')
import telegram

zoe_token = '770602880:AAGQsuy3uK-H5YCHqARjPKJnsmIIddwZ8TY'
zoe = telegram.Bot(token = zoe_token)

updates = zoe.getUpdates()
for u in updates:
    print(u.message)
