#Discord bot Create By firewax712

import discord
import os
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())

load_dotenv()

TOKEN = os.getenv('KEY')

@client.event
async def on_ready():
    print("Bot is ready")

client.run(TOKEN)