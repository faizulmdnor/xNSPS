import pandas as pd  # Import the pandas library for data manipulation
import numpy as np  # Import the numpy library for numerical operations


def load_data():
    """
    Loads death data from a CSV file into a pandas DataFrame.
    The CSV file is expected to be located at a predefined path and filename. The data is read using pandas' `read_csv` method.
    :return: A pandas DataFrame containing the death data from the CSV file.
    """
    # Define the file path where the CSV file is stored
    fpath = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/'
    # Define the file name of the CSV containing death data
    fname = "2001_2021_Death_by_state_sex_and_age_group_Malaysia.csv"
    # Combine the file path and file name to create the full file path
    filename = fpath + fname
    # Read the CSV data into a pandas DataFrame
    data = pd.read_csv(filename)
    return data


def number_of_death_is_int(df):
    """
    :param df: The input DataFrame that contains a 'Number of death' column to be processed.
    :return: A DataFrame with 'Number of death' column converted to integers, where NaN values are replaced by 0.
    """
    # Handle NaN values by converting the 'Number of death' column to numeric
    df['Number of death'] = pd.to_numeric(df['Number of death'], errors='coerce')
    # Fill NaN values in the 'Number of death' column with 0, and convert the column to integer type
    df['Number of death'] = df['Number of death'].fillna(0).astype(int)
    return df


data = load_data()
if data is not None:
    # Check if all necessary columns exist in the DataFrame
    required_columns = {'State', 'Year', 'Sex', 'Number of death'}
    if not required_columns.issubset(data.columns):
        print("Some required columns are missing from the data.")
    else:
        # Filter data for rows where the 'State' is 'Malaysia' (national death data)
        malaysia_death = data[data['State'] == 'Malaysia']
        malaysia_death = number_of_death_is_int(malaysia_death)

        # Filter data for rows where the 'State' is not 'Malaysia' (state-level death data)
        state_death = data[data['State'] != 'Malaysia']
        state_death = number_of_death_is_int(state_death)

        # Create a pivot table summarizing 'Number of death' by 'State' and 'Year'
        pivot_state_death = pd.pivot_table(
            state_death,
            index='State',
            columns='Year',
            values='Number of death',
            aggfunc='sum',
            fill_value=0
        )
        print(pivot_state_death)

        # Create a pivot table in the 'Number of death' by 'Sex' and 'Year'
        pivot_Malaysia_death_by_Sex = pd.pivot_table(
            malaysia_death,
            index='Sex',
            columns='Year',
            values='Number of death',
            aggfunc='sum',
            fill_value=0
        )
        print(pivot_Malaysia_death_by_Sex)

        # Calculate and print the total number of deaths by year for state-level data
        total_deaths_by_year_state = pivot_state_death.sum(axis=0)
        print("Total number of deaths by year (State-level):")
        print(total_deaths_by_year_state)

        # Calculate and print the total number of deaths by year for national data
        total_deaths_by_year_malaysia = pivot_Malaysia_death_by_Sex.sum(axis=0)
        print("Total number of deaths by year (National-level):")
        print(total_deaths_by_year_malaysia)
