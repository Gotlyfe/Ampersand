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

