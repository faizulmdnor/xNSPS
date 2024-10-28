import pyodbc
import pandas as pd

SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'Fezdbase'
conn = pyodbc.connect(f"DRIVER={{SQL Server}}; SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;")
cursor = conn.cursor()
#
# # Add department into Departments table in Database.
# dept = ['Finance', 'Human Resources', 'Information Technology', 'Marketing', 'Operations', 'Quality']
# for i in dept:
#     cursor.execute(f"INSERT INTO Departments (dept) VALUES (?)", (i,))
# conn.commit()

data = pd.read_csv('E:/X-NSPS/Python - Scripting/pythonProject/region_revenue_data.csv')

for i, r in data.iterrows():
    cursor.execute(f'INSERT INTO Region2 (date, Region_name, Revenue) VALUES (?, ?, ?)', r['date'], r['region'], r['revenue $'])
conn.commit()
conn.close()
