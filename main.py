import os
import json
import discord
import random
import requests
from discord.ext import commands


#will this show up to github

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_connect():
  print("your bot is online")

  
@bot.command()
async def NBA(ctx, *, cityChoice):
  url = "https://nba-stats4.p.rapidapi.com/teams/"

  querystring = {"per_page":"50","page":"1"}
  
  headers = {
  	"X-RapidAPI-Key": "c1b21959ccmshbee70286047ac69p13bf81jsn37520d1b50f7",
  	"X-RapidAPI-Host": "nba-stats4.p.rapidapi.com"
  }
  
  response = requests.request("GET", url, headers=headers, params=querystring)
  response = response.json()

  # cityNumber = -1
  # for i in range(30):
  #   if response[i]["city"].lower()==cityChoice.lower():
  #     cityNumber = i
  cityNumber = 0
  if cityNumber <= -1:
      await ctx.send("not an option, please try again")
  elif cityNumber > -1:
    for i in range(30):
      if response[i]["city"].lower()==cityChoice.lower():
        cityNumber = i
  else:
    await ctx.send("not an option, please try again")
  

  await ctx.send(response[cityNumber]["nickname"])

@bot.command()
async def currency(ctx, currency2, amount):
  url = "https://api.apilayer.com/exchangerates_data/convert?to="+currency2+"&from=USD&amount="+amount

  payload = {}
  headers= {
  "apikey": "nfd1NSoFEdpkuyAHDZkMK9oYA909Xgo1"
}

  response = requests.request("GET", url, headers=headers, data = payload)

  status_code = response.status_code
  result = response.json()

  rate=result["info"]["rate"]

  rate*=int(amount)
  
  await ctx.send(amount + "is" + rate + "in" + currency2 + "from USD")



my_secret = os.environ['TOKEN']
bot.run(my_secret)


