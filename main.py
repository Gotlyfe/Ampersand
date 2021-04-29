import discord

client = discord.client

@client.event
async def on_ready():
  print("We have logged in as " + client.user)

@client.event
async def on_message(message):
  if method.author = client.user:
    return
  
  if message.content.startswith("&help") or message.content.startswith("&?"):
    await message.channel.send("Help: <empty>")

client.run(os.getenv('TOKEN'))