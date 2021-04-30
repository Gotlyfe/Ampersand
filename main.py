#discord
import discord

#pypdf2
import PyPDF2
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

#file paths
import pathlib
from pathlib import Path

#url paths
import urllib.request

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



#character object
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
#discord client
client = discord.Client()
#object for writing pdfs
pdf_writer = PdfFileWriter()

#initializations
#random seed
random.seed(time.time())

#getting pdf from path
input_pdf = PdfFileReader("Character_Sheet_2018.pdf")

#ability scores strings
stat_strings = "Strength", "Dexterity", "Consitution", "Intelligence", "Wisdom", "Charisma"

#character basic info
character = Character("First Last",
	"Class",
	"Subclass",
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



def download_file(download_url):
    response = urllib.request.urlopen(download_url)
    file = open("Document.pdf", 'wb')
    file.write(response.read())
    file.close()
    #print("Completed")


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

		#Character Name
		canvas.setFont("Times-Roman", 16)
		canvas.drawString(0.2 * inch, 10.5 * inch, character.char_name)
		#Character level, class, background, and player name
		canvas.drawString(2 * inch, 10.5 * inch, str(character.char_level) + " " + character.char_subclass + ", " + character.char_class) 
		canvas.drawString(4.8 * inch, 10.5 * inch, character.char_background)
		canvas.drawString(6.5 * inch, 10.5 * inch, character.player_name)
		#Character Race, alignment, and experience
		canvas.drawString(2 * inch, 10 * inch, character.char_race)
		canvas.drawString(4.8 * inch, 10 * inch, character.char_alignment)
		canvas.drawString(6.5 * inch, 10 * inch, str(character.char_exp))

		#subtitles
		#character name
		canvas.setFont("Times-Roman", 8)
		canvas.drawString(0.5 * inch, 10.3 * inch, "Character Name")
		#Character level, class, background, and player name
		canvas.drawString(2 * inch, 10.3 * inch, "Level and Class")
		canvas.drawString(4.8 * inch, 10.3 * inch, "Background")
		canvas.drawString(6.5 * inch, 10.3 * inch, "Player Name")
		#Character Race, alignment, and experience
		canvas.drawString(2 * inch, 9.8 * inch, "Race")
		canvas.drawString(4.8 * inch, 9.8 * inch, "Alignment")
		canvas.drawString(6.5 * inch, 9.8 * inch, "Experience")

		#Attribute Names
		canvas.setFont("Times-Roman", 12)
		for count in range(0, 6):
			canvas.drawString(0.3 * inch, (9.75 * inch) - (count * inch), str(stat_strings[count]))
		#Attribute Values
		canvas.setFont("Times-Roman", 30)
		for count in range(0, 6):
			canvas.drawString(0.5 * inch, (9.25 * inch) - (count * inch), str(character.char_stats[count]))
		#Attribute modifier
		canvas.setFont("Times-Roman", 18)
		for count in range(0, 6):
			canvas.drawString(0.6 * inch, (9 * inch) - (count * inch), (str((character.char_stats[count] - 10)//2)))


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

		sendCharacterText = "pdf", "PDF", "Sheet", "sheet"
		for word in sendCharacterText:
			if message.content.startswith("&" + word):
				await SendSheet(message, character)


@client.event
async def on_reaction_add(reaction, user):
	if reaction.emoji == '😄':
		#do Stuff
		pass


client.run(os.getenv("TOKEN"))