import pandas as pd
from fezdbase import DataRetriever
import pyodbc


def get_data():
    """
    :return: Data retrieved from the database for the view vw_UserDetails
    """
    sql_query = '''
        SELECT *
        FROM vw_UserDetails
    '''
    data = DataRetriever.query_db(sql_query)
    return data


def generate_unique_username(username, cursor):
    """
    :param username: The base username that needs to be made unique.
    :param cursor: Database cursor used to execute SQL queries.
    :return: A unique username that does not exist in the Username table.
    """
    original_username = username
    counter = 1
    while True:
        cursor.execute("SELECT 1 FROM Username WHERE username = ?", (username,))
        if not cursor.fetchone():
            break
        username = f"{original_username}{counter}"
        counter += 1
        print(f'{username} new username generated.')
    return username


def insert_data(df):
    """
    :param df: DataFrame containing the data to insert into the database. The DataFrame must have 'userid' and 'username' columns.
    :return: None
    """
    server = 'FAIZULONXY\\SQLEXPRESS'  # Your server name
    database = 'Fezdbase'  # Your database name
    df['userid'] = df['userid'].astype(int).astype(object)
    df['username'] = df['username'].astype(str).astype(object)

    conn = pyodbc.connect(
        f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    try:
        for i in range(len(df)):
            userid = df.loc[i, 'userid']
            username = df.loc[i, 'username']
            unique_username = generate_unique_username(username, cursor)
            print(f"Inserting {userid}, {unique_username}")
            cursor.execute("INSERT INTO Username (userid, username) VALUES (?, ?)", (userid, unique_username))
        conn.commit()
        print("Data inserted successfully into Users table")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

df_data = get_data()
df_username = pd.DataFrame(columns=['userid', 'username'])
df_username['userid'] = df_data['userid']
df_username['username'] = df_data['firstname'].str.strip().str[:1] + df_data['lastname'].str.strip()
df_username['username'] = df_username['username'].str.lower()
insert_data(df_username)
