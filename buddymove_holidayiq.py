import sqlite3
import queries as q
import pandas as pd

# Step 1: Load the CSV file
csv_file = 'buddymove_holidayiq.csv'

# read the data from the csv
df = pd.read_csv(csv_file)

# look at the shape
print(df.shape)

# look at the head of the file
print(df.head())

# dataframe statistics
print(df.describe())

# learn more
print(df.info())

# check for missing values
print(df.isnull().sum())

def connect_to_db(db_name):
    return sqlite3.connect(db_file)

# define db file and table name
db_file = 'buddymove_holidayiq.sqlite3'
table_name = 'review'

def execute_q(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == '__main__':
    conn = connect_to_db(db_file)
    # check if review table already exists
    cursor = conn.cursor()
    cursor.execute(q.CHECK_IF_REVIEW_TABLE_EXISTS)
    table_exists = cursor.fetchone()
    # load data only if table does not exist
    if not table_exists:
        print(f"Table '{table_name}' does not exist. Loading data...")
        df.to_sql(table_name, conn, if_exists='fail', index=False)
        print(f"Data loaded into '{table_name}' table")
    else:
        print(f"Table '{table_name}' already exists. Skipping data load.")

    total_rows = execute_q(conn, q.BUDDYMOVE_COUNT_TOTAL_ROWS)
    total_rows_df = pd.DataFrame(total_rows)
    total_rows_df.columns = ['Total_Rows']
    print(total_rows_df)

    total_users_with_100_nature_and_shopping = execute_q(conn, q.BUDDYMOVE_TOTAL_USERS_WITH_100Nature_AND_100SHOPPING)
    total_users_with_100_nature_and_shopping_df = pd.DataFrame(total_users_with_100_nature_and_shopping)
    total_users_with_100_nature_and_shopping_df.columns = ['Total_Users']
    print(total_users_with_100_nature_and_shopping_df)

    avg_num_of_reviews_per_category = execute_q(conn, q.BUDDYMOVE_AVG_NUM_OF_REVIEWS_PER_CAT_PER_USER)
    avg_num_of_reviews_per_category_df = pd.DataFrame(avg_num_of_reviews_per_category)
    avg_num_of_reviews_per_category_df.columns = ['avg_sports_review_count', 'avg_religious_review_count', 'avg_nature_review_count', 'avg_theatre_review_count', 'avg_shopping_review_count', 'avg_picnic_review_count']
    print(avg_num_of_reviews_per_category_df)