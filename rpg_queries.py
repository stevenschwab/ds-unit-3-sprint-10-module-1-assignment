import sqlite3
import queries as q
import pandas as pd

def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    total_character_results = execute_q(conn, q.TOTAL_CHARACTERS)
    total_char_df = pd.DataFrame(total_character_results)
    total_char_df.columns = ['total_characters']
    print(total_char_df)

    total_subclass_results = execute_q(conn, q.TOTAL_SUBCLASS)
    total_subclass_df = pd.DataFrame(total_subclass_results)
    total_subclass_df.columns = ['Total_Necromancers', 'Total_Fighters', 'Total_Mages', 'Total_Thiefs', 'Total_Clerics']
    print(total_subclass_df)

    total_items_results = execute_q(conn, q.TOTAL_ITEMS)
    total_items_df = pd.DataFrame(total_items_results)
    total_items_df.columns = ['Total_Items']
    print(total_items_df)

    total_weapons_results = execute_q(conn, q.WEAPONS)
    total_weapons_df = pd.DataFrame(total_weapons_results)
    total_weapons_df.columns = ['Total_Weapons']
    print(total_weapons_df)

    total_non_weapons_results = execute_q(conn, q.NON_WEAPONS)
    total_non_weapons_df = pd.DataFrame(total_non_weapons_results)
    total_non_weapons_df.columns = ['Total_Non_Weapons']
    print(total_non_weapons_df)