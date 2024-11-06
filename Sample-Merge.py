import pandas as pd

irr_data = pd.read_csv('irradiance.csv')
temp_data = pd.read_csv('temp_data.csv')

temp_data.rename(columns={'Date':'Tarikh'}, inplace=True)

merge_temp_irr = pd.merge(irr_data, temp_data, left_on=['Date', 'Time'], right_on=['Tarikh', 'Time'], how='left')

print(merge_temp_irr)