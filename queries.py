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
# --------------buddymove_holidayiq queries--------------

CHECK_IF_REVIEW_TABLE_EXISTS = "SELECT name FROM sqlite_master WHERE type='table' AND name='review';"

# Count how many rows you have
BUDDYMOVE_COUNT_TOTAL_ROWS = """
    SELECT COUNT(*) AS Total_Rows
    FROM review;
"""

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
BUDDYMOVE_TOTAL_USERS_WITH_100Nature_AND_100SHOPPING = """
    SELECT COUNT(*) AS Total_Users
    FROM review
    WHERE Nature >= 100 AND Shopping >= 100;
"""

# What are the average number of reviews for each category?
BUDDYMOVE_AVG_NUM_OF_REVIEWS_PER_CAT_PER_USER = """
    SELECT AVG(Sports) AS avg_sports_review_count, 
        AVG(Religious) AS avg_religious_review_count, 
        AVG(Nature) AS avg_nature_review_count, 
        AVG(Theatre) AS avg_theatre_review_count, 
        AVG(Shopping) AS avg_shopping_review_count, 
        AVG(Picnic) AS avg_picnic_review_count
    FROM review;
"""