#discord
import discord
from discord.ext import commands

#environment
import os

#random
import random

#math
import math

#time
import time

#definitions






#Help Function "help", "Help", "tasukete", "Tasukete", "?"
async def Help(message):
	await message.add_reaction('🙌')
	helpChannel = await message.guild.create_text_channel('help' + str(random.randint(1, 8)))
	await message.channel.send("not here.")
	await helpChannel.send("...okay")
	await helpChannel.send("Whats up {}?".format(message.author.mention))


#Roll Function "roll", "Roll"
async def Roll(message):
	await message.add_reaction('🎲')
	await message.channel.send(random.randint(1, 6))


@client.event
async def on_ready():
	print("We have logged in as " + str(client.user))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith("&"):
		# message started with '&'

		helpText = "help", "Help", "tasukete", "Tasukete", "?"
		for word in helpText:
			if message.content.startswith("&" + word):
				await Help(message)

		diceText = "roll", "Roll"
		for word in diceText:
			if message.content.startswith("&" + word):
				await Roll(message)



@client.event
async def on_reaction_add(reaction, user):
	if reaction.emoji == '😄':
		#do Stuff
		pass
		
#instantiations

#initializations

#random seed
random.seed(time.time())

#discord client
client = discord.Client()


#main

#run discord client, connect using token
client.run(os.getenv("TOKEN"))