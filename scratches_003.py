import pandas as pd


def drop_rename_group(df):
    # Drop 'Lat' and 'Long' if they exist
    df.drop(columns=['Lat', 'Long'], errors='ignore', inplace=True)

    # Rename columns
    df.rename(columns={'Province/State': 'Province', 'Country/Region': 'Country'}, inplace=True)

    # Group by 'Country' and sum numeric columns
    df = df.groupby(['Country']).sum()

    # Drop 'Province' column if it exists
    df.drop(columns=['Province'], errors='ignore', inplace=True)

    return df

def daily_values(df):
    df_diff = df.diff(axis=1)
    df_diff.fillna(0, inplace=True)
    df_diff = df_diff.astype(int)
    return df_diff


# File paths
death = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/Covid19/time_series_covid19_deaths_global.csv'
confirmed = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/Covid19/time_series_covid19_confirmed_global.csv'
recovered = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/Covid19/time_series_covid19_recovered_global.csv'

# Read CSV files
df_death = pd.read_csv(death)
df_confirmed = pd.read_csv(confirmed)
df_recovered = pd.read_csv(recovered)

# Process each DataFrame
df_death = drop_rename_group(df_death)
df_confirmed = drop_rename_group(df_confirmed)
df_recovered = drop_rename_group(df_recovered)

# Print the processed DataFrames
print(df_confirmed)
print(df_recovered)
print(df_death)

df_daily_death = daily_values(df_death)
df_daily_confirmed = daily_values(df_confirmed)
df_daily_recovered = daily_values(df_recovered)

print(df_daily_death)
print(df_daily_confirmed)
print(df_daily_recovered)