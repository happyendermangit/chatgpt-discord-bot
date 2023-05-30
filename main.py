## MADE BY HAPPY ENDERMAN ##
## MADE BY HAPPY ENDERMAN ##
## MADE BY HAPPY ENDERMAN ##
## MADE BY HAPPY ENDERMAN ##

import discord
import openai 
from discord.ext import commands 
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='',intents=intents)
token = "" # Discord bot token 

channel_id = 0 # Channel id 
msgs = [{"role":"system",'content':'You are a chatbot that is like chatgpt and that help people.'}]
def chat(c):
    global msgs 
    openai.api_key = "" # Openai token
    msgs.append({"role":"user","content":c})
    cbot = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=msgs)
    msgs.append(cbot['choices'][0]['message'])
    return cbot['choices'][0]['message']['content']
@client.event 
async def on_ready():
    print("ready!",client.user)
@client.event 
async def on_message(msg):
    if msg.author.bot:
        return 
    else:
        if msg.channel.id == channel_id:
            a = await msg.channel.send('**Please wait...**')
            res = chat(msg.content)
            await a.edit(content='',embed=discord.Embed(title='Chatgpt :',description=f'**This uses openai api**\n> {msg.content}\n{res}'))
client.run(token)
