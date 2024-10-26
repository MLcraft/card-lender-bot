# This example requires the 'message_content' intent.
import logging

import discord
from discord.ext.commands import Bot


from services import external_lending_requests, external_user_requests
from commands.lender import Lender

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    await bot.add_cog(Lender(bot))
    print(f'We have logged in as {bot.user}')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     if message.content.startswith('$hello'):
#         userID = external_user_requests.getUserIdFromAPI(message.author.id)
#         print("-----------------------------------------------------------")
#         external_lending_requests.postLendCardFromOwnerToUser(userID, "cb418706-6703-4115-b174-0758b97e6f57", "0000419b-0bba-4488-8f7a-6194544ce91e", 4)
#         print("-----------------------------------------------------------")
#         external_lending_requests.getListCardsBorrowedByUser("cb418706-6703-4115-b174-0758b97e6f57")
#         print("-----------------------------------------------------------")
#         external_lending_requests.getListCardsLentByOwner(userID)
#         print("-----------------------------------------------------------")
#         await message.channel.send('Hello!')

bot.run('', log_level=logging.DEBUG)
