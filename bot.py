import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import re

#Scrape the riot website for the latest patch notes
def fetch():
    base_url = 'https://na.leagueoflegends.com'
    fetch_url = 'https://na.leagueoflegends.com/en-us/news/tags/patch-notes'
    html_page = urlopen(fetch_url)
    html_text = html_page.read().decode("utf-8")

    soup = BeautifulSoup(html_text, "html.parser")

    #Find the first link ,ie. the latest, patch notes
    for link in soup.find_all("a", limit=1):
        link_url = base_url + link["href"]

    link = "Latest patch: {}".format(link_url)     

    return link


load_dotenv()
#Get your discord bots token and paste it into the .env
TOKEN = os.getenv('DISCORD_TOKEN')

#Prefix for all the commands.
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#!patch for the latest league of legends patch notes
@bot.command(name='patch', help='Get the latest league of legends patch notes.')
async def patch(ctx):
    if ctx.author == bot.user:
        return

    response = fetch()

    await ctx.send(response)

bot.run(TOKEN)