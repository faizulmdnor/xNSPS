import pyodbc
import random
from faker import Faker

# Database connection details
server = 'FAIZULONXY\\SQLEXPRESS'  # Your server name
database = 'Fezdbase'  # Your database name

# Connect to the database
conn = pyodbc.connect(
    f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Initialize Faker to generate random names and dates
faker = Faker()

# Get list of genders and departments
cursor.execute("SELECT gid FROM Genders")
genders = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT deptid FROM Departments")
departments = [row[0] for row in cursor.fetchall()]

# Insert 500 random users
try:
    for _ in range(500):
        firstname = faker.first_name()
        lastname = faker.last_name()
        # Convert date_of_birth to a string in the format supported by SQL Server
        date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d')
        gender_id = random.choice(genders)
        deptid = random.choice(departments)

        # Use parameterized query to avoid SQL injection
        cursor.execute("""
            INSERT INTO Users (firstname, lastname, date_of_birth, gender_id, deptid)
            VALUES (?, ?, ?, ?, ?)
        """, (firstname, lastname, date_of_birth, gender_id, deptid))

    # Commit the transaction
    conn.commit()
    print("500 random users inserted into Users table.")

except Exception as e:
    # Rollback if there's an error
    conn.rollback()
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    cursor.close()
    conn.close()
