import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# Web server for uptime
app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Bot setup
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online 24/7 FOREVER!')
    await bot.change_presence(activity=discord.Game(name="Free Host 24/7"))

@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def hello(ctx):
    await ctx.send(f'👋 Hello {ctx.author.mention}! Bot is alive!')

@bot.command()
async def hack(ctx):
    await ctx.send("💀 Accessing mainframe...\n🔓 Bypassing firewall...\n📡 Injecting malware...\n✅ System compromised!")

# Start everything
keep_alive()
bot.run(os.environ['TOKEN'])
