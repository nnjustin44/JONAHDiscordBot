import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"]+" \n-"+json_data[0]["a"]
  return(quote)

@client.event
async def on_ready():
  print('We are logged on as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("!test"):
    await message.channel.send(" ```We are online sir``` ")

  if message.content.startswith("!thankyou"):
    await message.channel.send(" ```It's my pleasure sir``` ")

  if message.content.startswith("!id"):
    await message.channel.send(" ```J.O.N.A.H. V2 \n \nJustin's Online Native Artifical Helper \n \nMy original AI design was built by Mr. Nguyen using IBM's Watson Assistant. I have since been adapted to help serve the Couch Potatoes Discord Server with all needs``` ")

  if message.content.startswith("!inspire"):
    inspire = get_quote()
    await message.channel.send(inspire)

client.run(os.getenv('TOKEN'))
