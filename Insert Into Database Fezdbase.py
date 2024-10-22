import pyodbc
import pandas as pd

SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'Fezdbase2'
conn = pyodbc.connect(f"DRIVER={{SQL Server}}; SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;")
cursor = conn.cursor()
#
# # Add department into Departments table in Database.
# dept = ['Finance', 'Human Resources', 'Information Technology', 'Marketing', 'Operations', 'Quality']
# for i in dept:
#     cursor.execute(f"INSERT INTO Departments (dept) VALUES (?)", (i,))
# conn.commit()

data = pd.read_csv('E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/UserDetails.csv')

data['date_of_birth'] = pd.to_datetime(data['date_of_birth'])

for i, r in data.iterrows():
    cursor.execute(f"INSERT INTO Users (firstname, lastname, date_of_birth, gender_id, deptid) VALUES (?, ?, ?, ?, ?)",
                   (r['firstname'], r['lastname'], r['date_of_birth'], r['gender_id'], r['deptid']))
conn.commit()
conn.close()
