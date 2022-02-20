from telethon import TelegramClient , events , sync , connection
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)
import time
from bs4 import BeautifulSoup
import requests

print("")
api_id = 'api_id'
print("")
api_hash = 'api_hash'



client = TelegramClient(
    'session_name', api_id, api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=('server', port, 'secret'))
client.start()
    

try:
    @client.on(events.NewMessage)
    async def my_event_handler(event):
        if 'get_list_ponisha' in event.raw_text:
            print (event.raw_text)
            ses = requests.session()
            
            url = 'https://ponisha.ir/login'
            hed1 = {
                'user-agent': 'your user agent',
                
                'accept': 'application/json, application/json;q=0.8, text/plain;q=0.5, */*;q=0.2'
            }
            reqo = ses.get(url,headers=hed1)

            soup = BeautifulSoup(reqo.text, 'html.parser')
            csrf = soup.find("meta", {"name":"csrf-token"})['content']
            
            deta = '{"username":"your username","password":"your password"}'
            hed = {
                'user-agent': 'your user agent',
                'x-csrf-token': str(csrf),
                'accept': 'application/json, application/json;q=0.8, text/plain;q=0.5, */*;q=0.2',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '49',
                'content-type': 'application/json'

            }
            req = ses.post(url,data=deta,headers=hed)
            if req.text == '{"action":"redirect","url":"https:\/\/ponisha.ir\/dashboard"}':
                print("login")
                my_proj = ses.get('https://ponisha.ir/search/projects/my-skills')
                soup_proj = BeautifulSoup(my_proj.text, 'html.parser')
                for li in soup_proj.findAll("li", {"class":"item relative"}):
                    await event.reply(str(li.getText()))
                    print(li.getText())
            else:
                print('Wrong password')
                await event.reply('error')

except:
    pass
print("conect")

client.run_until_disconnected()




