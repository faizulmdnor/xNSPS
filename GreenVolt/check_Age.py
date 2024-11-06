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
data['status'] = data['Age'].apply(lambda age: 'inactive' if age >= 55 else 'active')

data.to_csv('E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/GreenVolt/employees_info.csv')
data_active = data[data['status'] == 'active']
data_active.drop(columns=['Date_of_Birth', 'Date_Hired', 'Position', 'Department', 'Site', 'Site_Country', 'status', 'Age', 'Hired_period'], inplace=True)
data_active.reset_index(drop=True, inplace=True)

df1 = data
df2 = data_active

df3_merge = pd.merge(df1, df2, left_on='emp_id', right_on='emp_id', how='left')
df4_merge = pd.merge(df1, df2, left_on='emp_id', right_on='emp_id', how='right')
df5_merge = pd.merge(df1, df2, left_on='emp_id', right_on='emp_id', how='inner')
df6_merge = pd.merge(df1, df2, left_on='emp_id', right_on='emp_id', how='outer')
df7_merge = df1.merge(df2, how='cross')

print(df3_merge)
print(df4_merge)