import pandas as pd

# Load the CSV file into a DataFrame
fpath = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/'
fname = 'UserDetails.csv'
f = fpath+fname
data = pd.read_csv(f)
df_data = pd.DataFrame(data)

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
df_data['nom_kp'] = df_data['b_code'].astype(str)+'-'+df_data['d_code'].astype(str)+"-"+df_data['g_code'].astype(str)
df_data2 = df_data[['userid', 'firstname', 'lastname', 'date_of_birth', 'gender', 'dept', 'nom_kp']]
# Print the updated DataFrame
print(df_data)
df_data2.to_csv(f'{fpath}UserDetailsWithICNumber.csv', index=False)
