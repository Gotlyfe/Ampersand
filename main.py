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

#input output
import io

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
	char_stats = stats(int, int, int, int, int, int)
	char_saving = saving_throw(int, int, int, int, int, int) # Used for saving throws for character
	char_saving_proficiency = saving_throw(int, int, int, int, int, int)
	char_skills = skills(int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int)
	char_skills_proficiency = skills(int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int)
	char_passive_perception: int
	char_inspiration: bool
	char_proficiency_bonus: int
	char_hp:int
	char_tmp_hp:int
	char_armor_class: int
	char_initiative: int
	char_speed: int
	char_hit_dice: int
	char_death_saves = death_saves(int, int)



#instantiation
#discord client
client = discord.Client()
#object for writing pdfs
pdf_writer = PdfFileWriter()

#initializations
#random seed
random.seed(time.time())


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
	1,)

character.char_stats = (10, 11, 12, 13, 14, 15)
character.char_saving =	(10, 11, 12, 13, 14, 15)	
character.char_saving_proficiency =	(1, 1, 0, 9, 0, 0)	
character.char_skills = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
character.char_skills_proficiency =	(0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
character.char_death_saves =(0, 0)

def download_file(download_url):
	response = urllib.request.urlopen(download_url)
	file = open("Document.pdf", 'wb')
	file.write(response.read())
	file.close()
	#print("Completed")

#creates a sheet for the character.pdf
def create_sheet(character):
	
	packet = io.BytesIO()
	# create a new PDF with Reportlab
	canvas = Canvas(packet, pagesize=LETTER)

	#Character Name
	canvas.setFont("Times-Roman", 16)
	canvas.drawString(0.7 * inch, 9.85 * inch, character.char_name)
	
	#Character level, class, background, and player name
	canvas.setFont("Times-Roman", 14)
	canvas.drawString(3.7 * inch, 10.15 * inch, str(character.char_level) + " " + character.char_subclass + ", " + character.char_class) 
	canvas.drawString(5.2 * inch, 10.15 * inch, character.char_background)
	canvas.drawString(6.5 * inch, 10.15 * inch, character.player_name)
	#Character Race, alignment, and experience
	canvas.drawString(3.7 * inch, 9.75 * inch, character.char_race)
	canvas.drawString(5.2 * inch, 9.75 * inch, character.char_alignment)
	canvas.drawString(6.5 * inch, 9.75 * inch, str(character.char_exp))


	#proficiency bonus
	canvas.setFont("Times-Roman", 24)
	canvas.drawString(1.35 * inch, (8.4 * inch), str(character.char_proficiency_bonus))

	#Armor Class
	canvas.drawString(3.2 * inch, (8.7 * inch), str(character.char_armor_class))

	#initiative
	canvas.drawString(4.0 * inch, (8.7 * inch), str(character.char_initiative))

	#speed
	canvas.drawString(4.75 * inch, (8.7 * inch), str(character.char_speed))

	#Attribute Values
	canvas.setFont("Times-Roman", 30)
	for count in range(0, 6):
		canvas.drawString(0.48 * inch, (8.55 * inch) - (count * inch), str(character.char_stats[count]))
	#Attribute modifier
	canvas.setFont("Times-Roman", 18)
	for count in range(0, 6):
		canvas.drawString(0.65 * inch, (8.22 * inch) - (count * inch), (str((character.char_stats[count] - 10)//2)))

	#Saving throws
	canvas.setFont("Times-Roman", 12)
	for count in range(0, 6):
		canvas.drawString(1.5 * inch, (8.0 * inch) - (count * inch * 0.188), (str((character.char_saving[count] - 10)//2)))
	#Saving throws proficiency
	canvas.setFont("Times-Roman", 6)
	for count in range(0, 6):
		canvas.drawString(1.33 * inch, (8.0 * inch) - (count * inch * 0.188), (str((character.char_saving_proficiency[count] - 10)//2)))

	#skills
	canvas.setFont("Times-Roman", 12)
	for count in range(0, 18):
		canvas.drawString(1.5 * inch, (6.4 * inch) - (count * inch * 0.188), (str((character.char_skills[count] - 10)//2)))
	#skills prof
	canvas.setFont("Times-Roman", 6)
	for count in range(0, 18):
		canvas.drawString(1.3 * inch, (6.4 * inch) - (count * inch * 0.188), (str((character.char_skills_proficiency[count] - 10)//2)))



	#save pdf
	canvas.save()

	#move to the beginning of the StringIO buffer
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	# read your existing PDF
	existing_pdf = PdfFileReader(open("Character_Sheet_2018.pdf", "rb"))
	output = PdfFileWriter()
	# add the "watermark" (which is the new pdf) on the existing page
	page = existing_pdf.getPage(0)	#only one page
	page.mergePage(new_pdf.getPage(0))
	output.addPage(page)
	# finally, write "output" to a real file
	outputStream = open("character.pdf", "wb")
	output.write(outputStream)
	outputStream.close()


#Help Function "help", "Help", "tasukete", "Tasukete", "?"
async def Help(message):
	await message.add_reaction('😄')
	await message.channel.send("no.")


#Roll Function "roll", "Roll"
async def Roll(message):
	await message.add_reaction('🎲')
	await message.channel.send(random.randint(1, 6))


#PDF charactersheet sending Function "pdf", "PDF"
async def SendSheet(message, character):
	#reaction to message 
	await message.add_reaction('📝')

	create_sheet(character)

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