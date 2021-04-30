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
pdf_writer = PdfFileWriter()
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

		#create pdf
		canvas = Canvas("character.pdf", pagesize=LETTER)
		canvas.setFont("Times-Roman", 18)
		canvas.drawString(72, 72, "Hello, World")
		#save pdf
		canvas.save()

		#send file to discord
		await message.channel.send(file=discord.File('character.pdf'))





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