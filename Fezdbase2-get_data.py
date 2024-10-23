import pyodbc
import pandas as pd
from matplotlib import pyplot as plt


SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'Fezdbase2'

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
cursor = conn.cursor()

tablename = 'vw_Users'

sql_query = f'SELECT * FROM {tablename}'

df_data = pd.read_sql(sql_query, conn)

df_male = df_data[df_data['gender'] == 'Male']
df_male.reset_index(drop=True, inplace=True)

df_female = df_data[df_data['gender'] == 'Female']
df_female.reset_index(drop=True, inplace=True)

# Initialize the d_code column with default value
df_data['d_code'] = 11

# Define a mapping for department codes
dept_codes = {
    'Quality': 33,
    'Finance': 44,
    'Human Resources': 66,
    'Information Technology': 77,
    'Marketing': 88,
    'Operations': 99
}

# Assign department codes based on the mapping
for dept, code in dept_codes.items():
    df_data.loc[df_data['dept'] == dept, 'd_code'] = code

# Convert d_code to integer type
df_data['d_code'] = df_data['d_code'].astype(int)

# Initialize gender count variables
m_count = 3030
f_count = 4039

# Initialize the g_code column
df_data['g_code'] = 0

# Assign g_code based on gender
for index, row in df_data.iterrows():
    if row['gender'] == 'Male':
        df_data.at[index, 'g_code'] = m_count
        m_count += 2
    elif row['gender'] == 'Female':
        df_data.at[index, 'g_code'] = f_count
        f_count += 2

df_data['date_of_birth'] = pd.to_datetime(df_data['date_of_birth'])
df_data['b_code'] = df_data['date_of_birth'].dt.strftime('%y%m%d')

# nom_kp is stand for 'Nombor Kad Pengenalan"
df_data['nom_kp'] = df_data['b_code'].astype(str) + '-' + df_data['d_code'].astype(str) + "-" + df_data[
    'g_code'].astype(str)
df_data2 = df_data[['userid', 'firstname', 'lastname', 'date_of_birth', 'gender', 'dept', 'nom_kp']]

# for i, r in df_data2.iterrows():
#     cursor.execute(
#         f'INSERT INTO User_noKP (userid, firstname, lastname, date_of_birth, gender, dept, nom_kp) VALUES (?, ?, ?, ?, ?, ?, ?)',
#         r['userid'], r['firstname'], r['lastname'], r['date_of_birth'], r['gender'], r['dept'], r['nom_kp'])
# conn.commit()
# conn.close()

# Count user IDs per department

dept_counts = df_data2['userid'].groupby(df_data2['dept']).count()

# Count user IDs per gender
gender_counts = df_data2['userid'].groupby(df_data2['gender']).count()

# First figure for department-wise count (line chart)
plt.figure(figsize=(8, 6))
plt.plot(dept_counts.index, dept_counts.values, marker='o')
plt.ylabel('Count of User IDs')
plt.xlabel('Department')
plt.title('Count of User IDs by Department in Fezdbase2 Database')
plt.xticks(rotation=45)  # Rotate labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Second figure for gender-wise count (bar chart)
plt.figure(figsize=(8, 6))
plt.bar(gender_counts.index, gender_counts.values)
plt.ylabel('Count of User IDs')
plt.xlabel('Gender')
plt.title('Count of User IDs by Gender in Fezdbase2 Database')
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()