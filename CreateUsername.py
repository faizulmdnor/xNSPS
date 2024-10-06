import pandas as pd
from fezdbase import DataRetriever


def get_data():
    # SQL query to fetch data from the view
    sql_query = '''
        SELECT *
        FROM vw_UserDetails
    '''

    # Fetch data using the static method from the class
    data = DataRetriever.query_db(sql_query)

    return data


df_data = get_data()

df_username = pd.DataFrame(columns=['userid', 'username'])
df_username['userid'] = df_data['userid']
df_username['username'] = df_data['firstname'].str.strip().str[:3] + df_data['lastname'].str.strip()
print(df_username)
