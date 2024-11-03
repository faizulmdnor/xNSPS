import pyodbc
import pandas as pd
from datetime import datetime

SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'GreenVolt'
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
cursor = conn.cursor()

# Fetch data from SQL
sql_query = """
    SELECT * FROM Employees 
    WHERE Date_Hired > DATEADD(YEAR, 1, GETDATE())
"""
data = pd.read_sql(sql_query, conn)

# Update dates in the DataFrame
new_dates = []
for date in data['Date_Hired']:
    # Convert to datetime format
    if isinstance(date, str):
        date_obj = datetime.strptime(date, '%Y-%m-%d')
    else:
        date_obj = date

    # Replace year with 1900s
    new_date_obj = date_obj.replace(year=int("19" + str(date_obj.year)[2:4]))
    new_dates.append(new_date_obj.strftime('%Y-%m-%d'))

# Assign the modified dates back to the DataFrame
data['Date_Hired'] = new_dates

# Update each row in the database
for index, row in data.iterrows():
    new_date = row['Date_Hired']
    empid = row['emp_id']

    sql_update = f"""
        UPDATE Employees
        SET Date_Hired = '{new_date}'
        WHERE emp_id = {empid}
    """

    # Execute the query with parameters
    try:
        cursor.execute(sql_update)
        conn.commit()  # Commit the update after each execution
    except Exception as err:
        print(f"Error updating emp_id {empid}: {err}")

# Close the connection
cursor.close()
conn.close()
