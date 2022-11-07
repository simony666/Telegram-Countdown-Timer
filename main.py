from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
from datetime import datetime
import schedule

API_ID = "API_ID"
API_HASH = "API_HASH"

def edit():
    now = datetime.now()
    diff = int((target - now).total_seconds())
    s = diff%60
    m = diff//60%60
    h = diff//60//60%24
    d = diff//60//60//24
    text = message.format(d,h,m,s)
    print(text)
    msg.edit(text)

if (name == "main"):
    client = TelegramClient('client', API_ID, API_HASH)
    target = datetime.fromtimestamp(1668562200)
    message = '''剩下 {} 天 {} 小时 {} 分钟 {} 秒
就到【11月16号 早上9点30分】了！'''

    client.start()
    print('Client Start')
    
    msg = client.get_messages(PeerChannel(1856928704), ids=297)
    print(msg)
    schedule.every(1).hours.do(edit)
    edit()
    #schedule.every(30).minutes.do(edit)
    #schedule.every(10).seconds.do(edit)
    while client.is_connected():
        schedule.run_pending()

client.run_until_disconnected()