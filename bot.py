# This example requires the 'message_content' intent.
import logging
import os
from dotenv import load_dotenv

import discord
from discord.ext.commands import Bot


from services import external_lending_requests, external_user_requests
from commands.lender import Lender

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    await bot.add_cog(Lender(bot))
    print(f'We have logged in as {bot.user}')

bot.run(os.getenv('DISCORD_BOT_TOKEN'), log_level=logging.DEBUG)
