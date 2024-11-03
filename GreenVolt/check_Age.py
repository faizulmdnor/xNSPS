import pandas as pd
import pyodbc


SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'GreenVolt'
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
cursor = conn.cursor()

# Fetch data from SQL
sql_query = """
    SELECT * FROM vw_Employees
"""
data = pd.read_sql(sql_query, conn)

# Convert 'Date_of_Birth' and 'Date_Hired' to datetime format
data['Date_of_Birth'] = pd.to_datetime(data['Date_of_Birth'], errors='coerce')
data['Date_Hired'] = pd.to_datetime(data['Date_Hired'], errors='coerce')

# Calculate age based on 'Date_of_Birth'
today = pd.to_datetime("today")
data['Age'] = (today - data['Date_of_Birth']).dt.days // 365.25
data['Hired_period'] = (today - data['Date_Hired']).dt.days // 365.25

# Handle NaN values in 'Age' and 'Hired_period' (if desired)
data['Age'].fillna(0, inplace=True)
data['Hired_period'].fillna(0, inplace=True)

data.to_csv('E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/GreenVolt/employees_info.csv', index=False)
