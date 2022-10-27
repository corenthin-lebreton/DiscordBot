import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!', description="bot description", intents=discord.Intents.all())

load_dotenv()
TOKEN = os.getenv('KEY')

@bot.event
async def on_ready():
    print("Bot is ready !")

@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx):
    await ctx.send("Combien de messages voulez-vous supprimer ?")

    def check(message):
       return message.author.id == ctx.message.author.id and message.channel == ctx.message.channel

    clearNumber = await bot.wait_for("message", check = check, timeout = 20)

    if clearNumber.content.isdigit() == False:
            await ctx.send("Désolé vous n'avez Veuillez rentrer un nombre valide")
    else:
        messages = await ctx.channel.purge(limit=int(clearNumber.content) + 1)
        
        channel = bot.get_channel(1033341730348605450)
    
        await channel.send(f"```{ctx.author} a supprimé {clearNumber.content} messages dans le channel {ctx.channel}```")









bot.run(TOKEN)