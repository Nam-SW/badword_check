import discord
import pandas as pd
from tensorflow.keras.models import load_model
import os

from utils.text import len_encode

base_url = os.getcwd()
client = discord.Client()
model = load_model(os.path.join(base_url, 'AI/model.h5'))
datadict = {'data':[], 'pred':[]}


def dict_reset():
    global datadict
    datadict = {'data':[], 'pred':[]}


@client.event
async def on_ready():
    print("================")
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    user_id = str(message.author.id)
    
    if message.author.bot:
        return

    if message.content:
        content = message.content
        if user_id == '426330292719058944' and content == '!수집':
            df = pd.DataFrame(datadict)
            path = os.path.join(base_url, 'data.xlsx')
            df.to_excel(path, index=None, encoding='utf-8-sig')
            await message.author.send(file=discord.File(path))
            os.remove(path)
            dict_reset()

        else:
            data = len_encode(content, 100)
            pred = model.predict(data)[0, 0]
            datadict['data'].append(content)
            datadict['pred'].append(pred)

    
        
def Bot_on():
    token = "NjY0Mzc0MjM5OTMwODc1OTA0.Xnw3LQ.gSjnG9fo56IWjEsngouq73kY7Rw"
    client.run(token)
