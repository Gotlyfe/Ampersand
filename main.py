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
#regex
import re


#instantiations

#discord client
client = commands.Bot(command_prefix = '&')


#initializations

#random seed
random.seed(time.time())


#Help Function "help", "Help", "tasukete", "Tasukete", "?"
async def Help(message):
	helpChannel = await message.guild.create_text_channel('help' + str(random.randint(1, 8)))
	await message.channel.send("not here.")
	await helpChannel.send("...okay")
	await helpChannel.send("Whats up {}?".format(message.author.mention))
	await message.add_reaction('🙌')




@client.event
async def on_ready():
	print("We have logged in as " + str(client.user))

@client.event
async def on_reaction_add(reaction, user):
	if(user != client):
		if reaction.emoji == '😄':
			#do Stuff
			await reaction.message.add_reaction('😄')
			
		if reaction.emoji == '😭':
			#do Stuff
			await reaction.message.add_reaction('😭')
		if reaction.emoji == '🎲':
			#do Stuff
			pass

#Ping Function
@client.command()
async def ping(context):
	await context.channel.send("Pong! {:.2g}".format(client.latency * 1000) + "ms")

	await context.message.add_reaction('🏓')


#mirror test command
@client.command()
async def test(ctx, arg):

  await ctx.send(arg)

#character
@client.command()
async def character(ctx, arg):
	arg = arg.lower()
	listOfCommands = [["create", "new", "add"],
	 ["delete", "remove"],
	  ["change", "swap", "switch"],
		 ["list", "all", "total"]]

	if arg in listOfCommands[0]:#"create", "new", "add"
		await ctx.send(listOfCommands[0])
	elif arg in listOfCommands[1]:#"delete", "remove"
		pass
	elif arg in listOfCommands[2]:#"change", "swap", "switch"
		pass
	elif arg in listOfCommands[3]:#"list", "all", "total"
		pass
	else:
		#print possible commands
		await ctx.send(listOfCommands)

#roll command
@client.command()
async def roll(ctx, *args):
	"""
	as &roll 2 d6
	"""
	await ctx.message.add_reaction('🎲')

	REQUIRED_NUMBER = 2
	
	if (len(args) != REQUIRED_NUMBER): #arguments not equal to required number
		await ctx.send("Invalid number of Arguments")
		return False

	try:
		total_rolls = int(args[0])
	except ValueError:
		await ctx.send(f"Invalid Argument 1: {args[0]}")

	if (args[1][0] == 'd'):
		command_str = "dice"
		dice_max = int(args[1][1:len(args[1])])
	else:
		await ctx.send(f"Invalid Argument 2: {args[1]}")
		return False

	args_str = f"({total_rolls},{dice_max})"
	try:
		rolls = eval(command_str+args_str)
	except NameError:
		await ctx.send("Something went wrong with evaluation")
		return False

	await ctx.send(rolls)
	await ctx.send(sum(rolls))



def dice(arg1, arg2):
	"""
	returns tuple size(arg1) each being randint between 1 and arg2
	"""
	rolls = []
	for count in range(arg1):
		rolls.append(random.randint(1,arg2))
	return rolls
#main

#run discord client, connect using token
client.run(os.getenv("TOKEN"))