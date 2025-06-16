# How many total characters are there?
TOTAL_CHARACTERS = 'SELECT COUNT(*) AS Total_Characters FROM charactercreator_character;'

# How many of each specific subclass (the necromancer table)?
TOTAL_SUBCLASS = '''
    SELECT
	(SELECT COUNT(*) FROM charactercreator_necromancer) AS Total_Necromancers,
	(SELECT COUNT(*) FROM charactercreator_fighter) AS Total_Fighters,
	(SELECT COUNT(*) FROM charactercreator_mage) AS Total_Mages,
	(SELECT COUNT(*) FROM charactercreator_thief) AS Total_Thiefs,
	(SELECT COUNT(*) FROM charactercreator_cleric) AS Total_Clerics;
'''

# How many total Items?
TOTAL_ITEMS = 'SELECT COUNT(*) AS Total_Items FROM armory_item;'

# How many of the Items are weapons?
WEAPONS = 'SELECT COUNT(*) as Total_Weapons FROM armory_weapon;'

# How many of the items are not weapons?
NON_WEAPONS = '''
    SELECT COUNT(*) FROM armory_item as ai
    LEFT JOIN armory_weapon as aw
    ON ai.item_id = aw.item_ptr_id
    WHERE item_ptr_id IS NULL;
'''

# How many Items does each character have? (Return first 20 rows)
CHARACTER_ITEMS = """
    SELECT cc_char.character_id, cc_char.name, COUNT(cc_char_i.item_id) AS Char_Item_Count
    FROM charactercreator_character cc_char
    LEFT JOIN charactercreator_character_inventory cc_char_i
    ON cc_char.character_id = cc_char_i.character_id
    GROUP BY cc_char.character_id
    LIMIT 20;
"""

# How many Weapons does each character have? (Return first 20 rows)
CHARACTER_WEAPONS = """
    SELECT cc_char.character_id, cc_char.name, COUNT(arm_w.item_ptr_id) AS Total_Weapons
    FROM charactercreator_character cc_char
    LEFT JOIN charactercreator_character_inventory cc_char_i
    ON cc_char.character_id = cc_char_i.character_id
    LEFT JOIN armory_weapon arm_w
    ON cc_char_i.item_id = arm_w.item_ptr_id
    GROUP BY cc_char.character_id
    LIMIT 20;
"""

# On average, how many Items does each Character have?
AVG_CHARACTER_ITEMS = """
    WITH char_item_counts AS (
        SELECT cc_char.character_id, cc_char.name, COUNT(cc_char_i.item_id) AS Char_Item_Count
        FROM charactercreator_character cc_char
        LEFT JOIN charactercreator_character_inventory cc_char_i
        ON cc_char.character_id = cc_char_i.character_id
        GROUP BY cc_char.character_id
    )
    SELECT AVG(Char_Item_Count) as avg_items_per_char
    FROM char_item_counts;
"""

# On average, how many Weapons does each character have?
AVG_CHARACTER_WEAPONS = """
    WITH total_weapons_per_char AS (
        SELECT cc_char.character_id, cc_char.name, COUNT(arm_w.item_ptr_id) AS Total_Weapons
        FROM charactercreator_character cc_char
        LEFT JOIN charactercreator_character_inventory cc_char_i
        ON cc_char.character_id = cc_char_i.character_id
        LEFT JOIN armory_weapon arm_w
        ON cc_char_i.item_id = arm_w.item_ptr_id
        GROUP BY cc_char.character_id
    )
    SELECT AVG(Total_Weapons) AS avg_weapons_per_char
    FROM total_weapons_per_char;
"""