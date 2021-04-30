import discord
import os

client = discord.Client()


@client.event
async def on_ready():
  print("We have logged in as " + str(client.user))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("&help") or message.content.startswith("&?"):
    await message.add_reaction('😄')
    await message.channel.send("no.")

@client.event
async def on_reaction_add(reaction, user):
  if reaction.emoji == '😄':
    #do Stuff


client.run(os.getenv('TOKEN'))