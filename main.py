import json
import os

import argparse
import asyncio
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

import discord

intents = discord.Intents.all()

cookies = json.loads(open("./bing_cookies_1.json", encoding="utf-8").read())  # might omit cookies option



# async def main():
#     parser = argparse.ArgumentParser(description='BingGPT CLI')
#     args = parser.parse_args()

    

#     while True:
#         message = input('Enter your message: ')
#         if message.lower() == 'quit':
#             break

#         response = await bot.ask(prompt=message, conversation_style=ConversationStyle.creative, simplify_response=True)
#         print(response['sources'])

class MyClient(discord.Client):

    #@client.event
    async def on_ready(self):
        self.chatbot = await Chatbot.create(cookies=cookies)
        print(f'Logged in as {client.user}')

    #@client.event
    async def on_message(self, message):

        if message.author == client.user:
            return
        if message.content.startswith('!GM'):
            print(message.content)
            response = await self.chatbot.ask(prompt=message.content + 'in at most 3 sentences', conversation_style=ConversationStyle.creative, simplify_response=True)
            print(response['sources'])
            await message.channel.send(response['sources'])

client = MyClient(intents=intents)

#change while deploying
client.run(os.environ['BOT_TOKEN'])

if __name__ == '__main__':
    asyncio.run(main())
