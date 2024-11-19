import pyodbc
import pandas as pd

# Load data
data = pd.read_csv('E:/X-NSPS/Python - Scripting/pythonProject/UserDetailsWithICNumber.csv')
df_data = data[['userid', 'nom_kp']]

# Define SQL Server connection details
server = 'FAIZULONXY\\SQLEXPRESS'  # Your server name
database = 'Fezdbase'  # Your database name
table = 'KadPengenalan'  # Table name

# Establish connection to SQL Server
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
cursor = conn.cursor()

# check data existence
select_query = f"SELECT * FROM {table}"
data_kp = cursor.execute(select_query).fetchall()
df_data_kp = pd.DataFrame(columns=['userid', 'nom_kp'])
df_data_kp['userid'] = [row[0] for row in data_kp]
df_data_kp['nom_kp'] = [row[1] for row in data_kp]
insert_query = f"INSERT INTO {table} (userid, nom_kp) VALUES (?, ?)"

# If df_data exist in df_data_kp
new_data = df_data.merge(df_data_kp, on=['userid', 'nom_kp'], how='left', indicator=True)
df_data_to_insert = new_data[new_data['_merge'] == 'left_only']

if df_data_to_insert.empty:
    print("No data to insert")
else:

    for index, row in df_data_to_insert.iterrows():
        cursor.execute(insert_query, row['userid'], row['nom_kp'])

# # Create an SQL insert query
#
# try:
#     # Insert each row from df_data into the SQL table
#     for index, row in df_data.iterrows():
#         cursor.execute(insert_query, row['userid'], row['nom_kp'])
#
#     # Commit the transaction
#     conn.commit()
#     print("Data inserted successfully.")
# except Exception as e:
#     # Rollback if there's an error
#     conn.rollback()
#     print(f"An error occurred: {e}")

# Close the connection
cursor.close()
conn.close()


