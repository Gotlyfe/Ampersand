#reportLab
import reportlab
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

#pypdf2
import PyPDF2
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

#object for writing pdfs
pdf_writer = PdfFileWriter()

#creates a sheet for the character.pdf
def create_sheet(character):
	
	packet = io.BytesIO()
	# create a new PDF with Reportlab
	canvas = Canvas(packet, pagesize=LETTER)

	#Character Name
	canvas.setFont("Times-Roman", 16)
	canvas.drawString(0.7 * inch, 9.85 * inch, character.char_name)
	
	#Character level, class, background, and player name
	canvas.setFont("Times-Roman", 12)
	canvas.drawString(3.7 * inch, 10.15 * inch, str(character.char_level) + " " + character.char_subclass + ", " + character.char_class) 
	canvas.drawString(5.2 * inch, 10.15 * inch, character.char_background)
	canvas.drawString(6.5 * inch, 10.15 * inch, character.player_name)
	#Character Race, alignment, and experience
	canvas.drawString(3.7 * inch, 9.75 * inch, character.char_race)
	canvas.drawString(5.2 * inch, 9.75 * inch, character.char_alignment)
	canvas.drawString(6.5 * inch, 9.75 * inch, str(character.char_exp))

	#hp
	canvas.setFont("Times-Roman", 8)
	canvas.drawString(4.2 * inch, (8.2 * inch), str(character.char_hp))

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
		canvas.drawString(1.5 * inch, (8.0 * inch) - (count * inch * 0.188), (str(character.char_saving[count])))
	#Saving throws proficiency
	canvas.setFont("Times-Roman", 6)
	for count in range(0, 6):
		canvas.drawString(1.33 * inch, (8.0 * inch) - (count * inch * 0.188), (str(character.char_saving_proficiency[count])))

	#skills
	canvas.setFont("Times-Roman", 12)
	for count in range(0, 18):
		canvas.drawString(1.5 * inch, (6.4 * inch) - (count * inch * 0.188), (str(character.char_skills[count])))
	#skills prof
	canvas.setFont("Times-Roman", 6)
	for count in range(0, 18):
		canvas.drawString(1.33 * inch, (6.4 * inch) - (count * inch * 0.188), (str(character.char_skills_proficiency[count])))



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

def create_mini_sheet(character):
	# create a new PDF with Reportlab
	packet = io.BytesIO()
	canvas = Canvas("mini_character.pdf", pagesize=(12 * inch, 16 * inch))

	attribute_strings = ("Strength", "Dexterity", "Consitution", "Intelligence", "Wisdom", "Charisma")
	skill_strings = ("Acrobatics", "Animal_handling", "Arcana", "Athletics", "Deception", "History", "Insight",
	"Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival")


	#Character Name
	canvas.setFont("Times-Roman", 24)
	canvas.drawString(0.8 * inch, 15.5 * inch, character.char_name)
	canvas.drawString(9 * inch, 15.5 * inch, character.player_name)
	
	#Character level, class, background, and player name
	#Character Race, alignment, and experience
	canvas.setFont("Times-Roman", 20)
	canvas.drawString(1 * inch, 13.5 * inch, str(character.char_level) + " " + character.char_subclass + ", " + character.char_class) 
	canvas.drawString(3.5 * inch, 13.5 * inch, character.char_background)
	canvas.drawString(6 * inch, 13.5 * inch, character.char_alignment)
	canvas.drawString(8.5 * inch, 13.5 * inch, character.char_race)
	canvas.drawString(11 * inch, 13.5 * inch, str(character.char_exp))


	canvas.setFont("Times-Roman", 18)
	canvas.drawString(4.0 * inch, (8.2 * inch), str(character.char_hp))


	#proficiency bonus
	canvas.drawString(7.65 * inch, (9.4 * inch), str("Proficiency:"))
	canvas.setFont("Times-Roman", 32)
	canvas.drawString(7.85 * inch, (9.6 * inch), str(character.char_proficiency_bonus))

	#Armor Class
	canvas.drawString(7.2 * inch, (8.7 * inch), str(character.char_armor_class))

	#initiative
	canvas.drawString(7.0 * inch, (8.7 * inch), str(character.char_initiative))

	#speed
	canvas.drawString(7.75 * inch, (8.7 * inch), str(character.char_speed))

	#Attribute Values
	canvas.setFont("Times-Roman", 40)
	for count in range(0, 6):
		canvas.drawString(0.7 * inch + (inch * count * 2), (14 * inch) - (inch * 1.5), str(character.char_stats[count]))
	#Attribute modifier
	canvas.setFont("Times-Roman", 32)
	for count in range(0, 6):
		canvas.drawString(0.7 * inch + (inch * count * 2), (14 * inch) - (inch * 2.0), (str((character.char_stats[count] - 10)//2)))
	#Attribute strings
	for count in range(0, 6):
		canvas.drawString(0.5 * inch + (inch * count * 2), (14 * inch) - (inch * 1.0), attribute_strings[count])

	#Saving throws
	canvas.setFont("Times-Roman", 24)
	for count in range(0, 6):
		canvas.drawString(0.8 * inch + (inch * count * 2), (13 * inch) - (inch * 2.0), (str(character.char_saving[count])))
	#Saving throws proficiency
	canvas.setFont("Times-Roman", 12)
	for count in range(0, 6):
		canvas.drawString(0.8 * inch + (inch * count * 2), (13 * inch) - (inch * 2.0), (str(character.char_saving_proficiency[count])))

	#skills
	canvas.setFont("Times-Roman", 32)
	for count in range(0, 18):
		canvas.drawString(0.8 * inch, (12.7 * inch) - (count * inch * 0.7), (str(character.char_skills[count])))
	#skills prof
	canvas.setFont("Times-Roman", 18)
	for count in range(0, 18):
		canvas.drawString(0.5 * inch, (12.8 * inch) - (count * inch * 0.7), (str(character.char_skills_proficiency[count])))
	#skills string
	canvas.setFont("Times-Roman", 24)
	for count in range(0, 18):
		canvas.drawString(1.3 * inch, (12.7 * inch) - (count * inch * 0.7), (str(skill_strings[count] )))


	#save pdf
	canvas.save()

#PDF charactersheet sending Function "pdf", "PDF"
async def SendSheet(message, character):
	#reaction to message 
	await message.add_reaction('📝')


	#send file to discord
	await message.channel.send(file=discord.File('character.pdf'))

	#delete saved file
	#os.remove('character.pdf')