import pyodbc
import pandas as pd

SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'Fezdbase2'

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')

tablename = 'vw_Users'

sql_query = f'SELECT * FROM {tablename}'

df_data = pd.read_sql(sql_query, conn)

df_male = df_data[df_data['gender'] == 'Male']
df_male.reset_index(drop=True, inplace=True)
print(df_male)

df_female = df_data[df_data['gender'] == 'Female']
df_female.reset_index(drop=True, inplace=True)
print(df_female)

dept_code = {'Quality': 33,
          'Finance': 44,
          'Human Resources': 66,
          'Information Technology': 77,
          'Marketing': 88,
          'Operations': 99}

