import pandas as pd
filepath = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/'
filename = '2001_2021_Death_by_state_sex_and_age_group_Malaysia.csv'
f = filepath+filename
data = pd.read_csv(f)
df_data = pd.DataFrame(data)

# by State
death_by_state = df_data[df_data['State'] != 'Malaysia']
malaysia_death = df_data[df_data['State'] == 'Malaysia']
malaysia_death = malaysia_death[['Year', 'Age group', 'Sex', 'Number of death']]

malaysia_death_by_gender = malaysia_death.groupby(by=['Year', 'Age group', 'Sex']).sum()
print(malaysia_death_by_gender)

death_by_state = death_by_state.groupby(by=['Year', 'State'], dropna=False).sum('Number of death')
death_by_state['Number of death'] = pd.to_numeric(death_by_state['Number of death'], errors='coerce')
death_by_state['Number of death'] = death_by_state['Number of death'].fillna(0).astype(int)
print(death_by_state)