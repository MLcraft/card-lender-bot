# This example requires the 'message_content' intent.
import logging

import discord
from discord.ext.commands import Bot


from services import external_lending_requests, external_user_requests
from commands import Lender

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        userID = external_user_requests.getUserIdFromAPI(message.author.id)
        print("-----------------------------------------------------------")
        external_lending_requests.postLendCardFromOwnerToUser(userID, "26ce6475-9666-44e8-bc0a-b78316688278", "0000419b-0bba-4488-8f7a-6194544ce91e", 4)
        print("-----------------------------------------------------------")
        external_lending_requests.getListCardsBorrowedByUser("26ce6475-9666-44e8-bc0a-b78316688278")
        print("-----------------------------------------------------------")
        external_lending_requests.getListCardsLentByOwner(userID)
        print("-----------------------------------------------------------")
        await message.channel.send('Hello!')

bot.add_cog(Lender(bot))
bot.run('', log_level=logging.DEBUG)
