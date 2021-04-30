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

import dataclasses
from dataclasses import dataclass
from collections import namedtuple

@dataclass
class Character():
	#Character stats at base values
	stats = namedtuple("Stats", ["strength", "dexterity", "consitution", "intelligence", "wisdom", "charisma"])

	#Saving throws base values
	saving_throw = namedtuple("Saving_Throw", ["strength", "dexterity", "consitution", "intelligence", "wisdom", "charisma"])

	#Skills unmodified
	skills = namedtuple("Skills", ["acrobatics", "animal_handling", "arcana", "athletics", "deception", "history", "insight",
	"intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion", "religion", "sleight_of_hand", "stealth", "survival"])

	# death_saves will be passed a tuple of (bool, bool, bool)
	death_saves = namedtuple("Death_Saves", ["successes", "failures"])

	#Character General Info
	char_name: str
	char_class: str
	char_subclass: str
	char_background: str
	player_name: str #This will be thier discord tag
	char_race: str
	char_alignment: str
	char_exp: int
	char_level: int

	#Character Action Stats
	char_stats = stats(10, 10, 10, 10, 10, 10)
	char_saving = saving_throw(0, 0, 0, 0, 0, 0) # Used for saving throws for character
	char_skills = skills(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	char_passive_perception: int
	char_inspiration: bool
	char_proficiency_bonus: int
	char_hp:int
	char_tmp_hp:int
	char_armor_class: int
	char_initiative: int
	char_speed: int
	char_hit_dice: int
	char_death_saves = death_saves(0, 0)


#instantiation
client = discord.Client()

#initializations
random.seed(time.time())


pChar = Character("First Last",
	"Class Name",
	"Subclass Name",
	"Background",
	"Discord Name",
	"Sub Race, Race",
	"Alignment",
	0,
	0,
	12,
	False,
	2,
	6,
	0,
	10,
	0,
	30,
	1)



#Help Function "help", "Help", "tasukete", "Tasukete", "?"
async def Help(message):
		await message.add_reaction('😄')
		await message.channel.send("no.")


#Roll Function "roll", "Roll"
async def Roll(message):
		await message.add_reaction('🎲')
		await message.channel.send(random.randint(1, 6))


#PDF sending Function "pdf", "PDF"
async def SendSheet(message, character):
		await message.add_reaction('📝')

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




@client.event
async def on_ready():
	print("We have logged in as " + str(client.user))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith("&"):
		# message started with '&'

		helpText = "h", "H", "help", "Help", "tasukete", "Tasukete", "?"
		for word in helpText:
			if message.content.startswith("&" + word):
				await Help(message)

		diceText = "r", "R", "roll", "Roll"
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