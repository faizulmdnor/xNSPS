import pandas as pd  # Import the pandas library for data manipulation
import numpy as np   # Import the numpy library for numerical operations

# Define the file path where the CSV file is stored
fpath = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/'

# Define the file name of the CSV containing death data
fname = "2001_2021_Death_by_state_sex_and_age_group_Malaysia.csv"

# Combine the file path and file name to create the full file path
filename = fpath + fname

# Read the CSV data into a pandas DataFrame
data = pd.read_csv(filename)

# Filter data for rows where the 'State' is 'Malaysia' (national death data)
malaysia_death = data[data['State'] == 'Malaysia']

# Filter data for rows where the 'State' is not 'Malaysia' (state-level death data)
state_death = data[data['State'] != 'Malaysia']

# Handle NaN values by converting the 'Number of death' column to numeric
# Any non-numeric values will be coerced to NaN
state_death['Number of death'] = pd.to_numeric(state_death['Number of death'], errors='coerce')

# Fill NaN values in the 'Number of death' column with 0, and convert the column to integer type
state_death['Number of death'] = state_death['Number of death'].fillna(0).astype(int)

# Create a pivot table summarizing 'Number of death' by 'State' and 'Year'
# The table will show the sum of deaths for each state by year, with 0 as the default fill value
pivot_state_death = pd.pivot_table(
    state_death,          # DataFrame to pivot
    index='State',         # Rows will represent 'State'
    columns='Year',        # Columns will represent 'Year'
    values='Number of death',  # Values to summarize
    aggfunc='sum',         # Aggregation function to sum deaths for each group
    fill_value=0           # Fill missing values with 0
)

# Print the resulting pivot table
print(pivot_state_death)
