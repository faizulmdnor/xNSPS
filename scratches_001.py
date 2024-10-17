import pandas as pd  # Importing the pandas library for data manipulation and analysis.
import pyodbc  # Importing pyodbc to connect and interact with a SQL database.

def insert_data(table_name, df, conn):
    # Defining a function to insert data into a SQL table. It takes the table name, a DataFrame, and a connection object as input.
    columns = ', '.join(df.columns)
    # Creating a string of column names separated by commas.
    placeholder = ', '.join('?' * len(df.columns))
    # Creating placeholders for parameterized queries to prevent SQL injection. It generates '?' for each column.
    sql_insert = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholder})"
    # Building the SQL INSERT statement dynamically with the table name and columns.

    # Using a context manager to handle cursor
    # This ensures the cursor is closed after execution, even if an exception occurs.
    try:
        # Start of the try block to handle any potential exceptions during database interaction.
        with conn.cursor() as cursor:
            # Opening a cursor object to execute SQL commands.
            for _, row in df.iterrows():
                # Iterating over each row of the DataFrame.
                cursor.execute(sql_insert, tuple(row))
                # Executing the SQL insert statement for each row.
            conn.commit()
            # Committing the transaction to save changes in the database.
            print(f"Data inserted into {table_name} SUCCESS")
            # Printing success message if the data insertion is successful.
    except Exception as e:
        # Catching any exception that occurs during the process.
        print(f"Data insertion FAIL into {table_name} table. {e}")
        # Printing a failure message with the error details.
        conn.rollback()
        # Rolling back the transaction in case of failure.

# Defining the country data as a dictionary.
country = {
    'country_id': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],
    'Country': ['Malaysia', 'Indonesia', 'Germany', 'Guyana', 'Canada', 'Luxembourg', 'Australia', 'Namibia',
                'New Zealand', 'Poland', 'Columbia', 'Singapore', 'Spain', 'Thailand', 'Vietnam']
}

# Defining the sites data with their associated countries.
sites = {
    'site_id': [1001, 1002, 1003, 2001],
    'country_id': [1000, 1000, 1000, 2000],
    'Site': ['Kuala Lumpur', 'Kulim', 'Senai', 'Surabaya']
}

# Defining departments with unique IDs.
departments = {
    'dept_id': [1010, 2010, 3010, 4010, 5010, 6010, 7010, 8010, 9010, 9050],
    'Department': ['Data Analysis', 'Engineering', 'Executive Management', 'Finance', 'Human Resource',
                    'Information Technology', 'Safety', 'Sales', 'Site Management', 'Site Support']
}

# Defining positions along with department relationships.
positions = {
    'pos_id': [3011, 3012, 3013, 1011, 1012, 1013, 1014, 2011, 2012, 2013, 2014, 3014, 3015, 3016, 3017, 4011, 4012,
               4013, 4014, 5011, 5012, 5013, 5014, 6011, 6012, 6013, 6014, 9011, 9012, 7011, 7012, 7013, 7014, 8011,
               8012, 8013, 8014, 9013, 9014, 9015, 9016, 9017, 9051, 9052, 9053, 9054, 9018],
    'dept_id': [3010, 3010, 3010, 1010, 1010, 1010, 1010, 2010, 2010, 2010, 2010, 3010, 3010, 3010, 3010, 4010, 4010,
                4010, 4010, 5010, 5010, 5010, 5010, 6010, 6010, 6010, 6010, 9010, 9010, 7010, 7010, 7010, 7010, 8010,
                8010, 8010, 8010, 9010, 9010, 9010, 9010, 9010, 9050, 9050, 9050, 9050, 9010],
    'Position': ['Chief Executive Officer', 'Chief Financial Officer', 'Chief Information Officer',
                 'Data Analysis Analyst', 'Data Analysis Engineer', 'Data Analysis Executive', 'Data Analysis Manager',
                 'Engineering Analyst', 'Engineering Engineer', 'Engineering Executive', 'Engineering Manager',
                 'Executive Management Analyst', 'Executive Management Engineer', 'Executive Management Executive',
                 'Executive Management Manager', 'Finance Analyst', 'Finance Engineer', 'Finance Executive',
                 'Finance Manager', 'HR Analyst', 'HR Engineer', 'HR Executive', 'HR Manager',
                 'Information Technology Analyst', 'Information Technology Engineer',
                 'Information Technology Executive', 'Information Technology Manager', 'Kuala Lumpur Site Manager',
                 'Kulim Site Manager', 'Safety Analyst', 'Safety Engineer', 'Safety Executive', 'Safety Manager',
                 'Sales Analyst', 'Sales Engineer', 'Sales Executive', 'Sales Manager', 'Senai Site Manager',
                 'Site Management Analyst', 'Site Management Engineer', 'Site Management Executive',
                 'Site Management Manager', 'Site Support Analyst', 'Site Support Engineer', 'Site Support Executive',
                 'Site Support Manager', 'Surabaya Site Manager']
}

# Reading employee data from a CSV file and creating a DataFrame.
employees = pd.read_csv('E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/Data/Employees.csv')
df_employees = pd.DataFrame(employees)
# Converting the 'employees' dictionary into a pandas DataFrame.
df_country = pd.DataFrame(country)
# Creating a DataFrame for country data.
df_sites = pd.DataFrame(sites)
# Creating a DataFrame for sites data.
df_departments = pd.DataFrame(departments)
# Creating a DataFrame for departments data.
df_positions = pd.DataFrame(positions)
# Creating a DataFrame for positions data.
df_employees['Date_of_Birth'] = pd.to_datetime(df_employees['Date_of_Birth'])
# Converting 'Date_of_Birth' column in employee DataFrame to datetime format.
df_employees['Date_Hired'] = pd.to_datetime(df_employees['Date_Hired'])
# Converting 'Date_Hired' column in employee DataFrame to datetime format.

server = 'FAIZULONXY\\SQLEXPRESS'  # Specifying the SQL Server instance.
database = 'GreenVolt'  # Specifying the database name.

conn = pyodbc.connect(
    f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)
# Establishing a connection to the SQL Server database using pyodbc.

try:
    # insert_data('Country', df_country, conn)  # Uncomment to insert country data into SQL table.
    # insert_data('Sites', df_sites, conn)  # Uncomment to insert sites data into SQL table.
    # insert_data('Departments', df_departments, conn)  # Uncomment to insert departments data into SQL table.
    # insert_data('Positions', df_positions, conn)  # Uncomment to insert positions data into SQL table.
    # insert_data('Employees', df_employees, conn)  # Uncomment to insert employees data into SQL table.
    print('Enable line above to insert data into table.')
    # Reminder message to uncomment lines when ready to insert data into the database.

finally:
    conn.close()
    # Ensuring the database connection is closed after the operation, even if an error occurs.
