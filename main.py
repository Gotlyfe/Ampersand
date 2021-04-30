#discord
import discord

#pypdf2
import PyPDF2 

#file paths
import pathlib


#reportLab
import reportlab
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

#environment
import os

#random
import random

#math
import math

#time
import time


#instantiation
client = discord.Client()

#initializations
random.seed(time.time())



#Help Function "help", "Help", "tasukete", "Tasukete", "?"
async def Help(message):
		await message.add_reaction('😄')
		await message.channel.send("no.")


#Roll Function "roll", "Roll"
async def Roll(message):
		await message.add_reaction('🎲')
		await message.channel.send(random.randint(1, 6))


#PDF sending Function "pdf", "PDF"
async def SendPDF(message):
		await message.add_reaction('📝')

		attributeStrings = ("Strength", "Str"), ("Dexterity", "Dex"), ("Constitution", "Con"), ("Intelligence", "Int"), ("Wisdom", "Wis"), ("Charisma", "Cha")
		attributes = strength, dexterity, constitution, intelligence, wisdom, charisma = 8, 10, 10, 12, 14, 15

		#create pdf
		canvas = Canvas("character.pdf", pagesize=LETTER)
		canvas.setFont("Times-Roman", 12)
		for count in range(0, 6):
			canvas.drawString(0.5 * inch, (10.75 * inch) - (count * inch), (attributeStrings[count][0]))
		canvas.setFont("Times-Roman", 30)
		for count in range(0, 6):
			canvas.drawString(0.5 * inch, (10.25 * inch) - (count * inch), (str(attributes[count])))
		canvas.setFont("Times-Roman", 20)
		for count in range(0, 6):
			canvas.drawString(0.75 * inch, (10 * inch) - (count * inch), (str((attributes[count] - 10)//2)))
		#save pdf
		canvas.save()

		#send file to discord
		await message.channel.send(file=discord.File('character.pdf'))

		#delete saved file
		#os.remove('character.pdf')





def npcSheet():
	#character's names
	name = []
	attributeStrings = ("Strength", "Str"), ("Dexterity", "Dex"), ("Constitution", "Con")
	attributes = strength, dexterity, constitution
	classStrings = "Cleric", "Fighter", "Rogue", "Wizard"



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

		sendPDFText = "pdf", "PDF"
		for word in sendPDFText:
			if message.content.startswith("&" + word):
				await SendPDF(message)


@client.event
async def on_reaction_add(reaction, user):
	if reaction.emoji == '😄':
		#do Stuff
		pass


client.run(os.getenv("TOKEN"))