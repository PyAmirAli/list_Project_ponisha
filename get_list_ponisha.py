from telethon import TelegramClient , events , sync , connection
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)
import time
from bs4 import BeautifulSoup
import requests
print("""get Project list in site irani ponisha.ir send to telegram""")
print("")
print("""Information account telegram
api_id and api_hash
""")
print("")
api_id = input('api_id--->')
print("")
api_hash = input("api_hash--->")
print("Proxy information")
print("")
server = input('server -->')
port = input('port -->')
secret = input('secret -->')
client = TelegramClient(
    'session_name', api_id, api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=(server, port, secret))
client.start()
try:
    @client.on(events.NewMessage)
    async def my_event_handler(event):
        if 'get_list_ponisha' in event.raw_text:
            print (event.raw_text)
            site = requests.get('https://ponisha.ir/search/projects/skill-python/status-open')
            soup = BeautifulSoup(site.text, 'html.parser')
            for li in soup.findAll("li", {"class":"item"}):
                try:
                    text = (li.getText())
                    print(text)
                    await event.reply(str(text))
                except:
                    await event.reply('error')
except:
    pass
print("conect")
client.run_until_disconnected()
