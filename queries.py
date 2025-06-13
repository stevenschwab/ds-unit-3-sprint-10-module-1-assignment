# How many total characters are there?
TOTAL_CHARACTERS = 'SELECT COUNT(*) AS Total_Characters FROM charactercreator_character;'

# How many of each specific subclass (the necromancer table)?
TOTAL_SUBCLASS = '''
    SELECT
	(SELECT COUNT(*) FROM charactercreator_necromancer) AS Total_Necromancers,
	(SELECT COUNT(*) FROM charactercreator_fighter) AS Total_Fighters,
	(SELECT COUNT(*) FROM charactercreator_mage) AS Total_Mages,
	(SELECT COUNT(*) FROM charactercreator_thief) AS Total_Thiefs,
	(SELECT COUNT(*) FROM charactercreator_cleric) AS Total_Clerics
'''

# How many total Items?
TOTAL_ITEMS = 'SELECT COUNT(*) AS Total_Items FROM armory_item'

# How many of the Items are weapons?
WEAPONS = ''

# How many of the items are not weapons?
NON_WEAPONS = ''

# How many Items does each character have? (Return first 20 rows)
CHARACTER_ITEMS = ''

# How many Weapons does each character have? (Return first 20 rows)
CHARACTER_WEAPONS = ''

# On average, how many Items does each Character have?
AVG_CHARACTER_ITEMS = ''

# On average, how many Weapons does each character have?
AVG_CHARACTER_WEAPONS = ''