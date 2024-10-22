import wget
import pandas as pd
import os
import numpy as np

#download data from URLs:

urls = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv']

path = 'D:\Faizul - Python\Covid19'

for url in urls:
    filename = path + '/' + os.path.basename(url)
    if os.path.exists(filename):
        os.remove(filename) #remove existing file.
    wget.download(url, out=filename)

#read downloaded files
confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
death_df = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('time_series_covid19_recovered_global.csv')

dates = confirmed_df.columns[4:]

confirmed_df_long = confirmed_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=dates,
    var_name='Date',
    value_name='Confirmed'
)

death_df_long = death_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=dates,
    var_name='Date',
    value_name='Deaths'
)

recovered_df_long = recovered_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=dates,
    var_name='Date',
    value_name='Recovered'
)

recovered_df_long = recovered_df_long[recovered_df_long['Country/Region']!='Canada']

#Merging confirmed_df_long and death_df_long

full_table = confirmed_df_long.merge(
    right=death_df_long,
    how='left',
    on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)

#Merging full_table and recovered_df_long
full_table = full_table.merge(
    right=recovered_df_long,
    how='left',
    on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)

full_table['Date'] = pd.to_datetime(full_table['Date'])

full_table['Recovered'] = full_table['Recovered'].fillna(0)

ship_rows = full_table['Province/State'].str.contains('Grand Princess') | full_table['Province/State'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('MS Zaandam')
full_ship = full_table[ship_rows]

full_table = full_table[~(ship_rows)]

#active cases = confirmed - death - recovered
full_table['Active'] = full_table['Confirmed'] - full_table['Deaths'] - full_table['Recovered']


full_grouped = full_table.groupby(['Date', 'Country/Region'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()

# new cases
temp = full_grouped.groupby(['Country/Region', 'Date', ])['Confirmed', 'Deaths', 'Recovered']
temp = temp.sum().diff().reset_index()
mask = temp['Country/Region'] != temp['Country/Region'].shift(1)
temp.loc[mask, 'Confirmed'] = np.nan
temp.loc[mask, 'Deaths'] = np.nan
temp.loc[mask, 'Recovered'] = np.nan
# renaming columns
temp.columns = ['Country/Region', 'Date', 'New cases', 'New deaths', 'New recovered']
# merging new values
full_grouped = pd.merge(full_grouped, temp, on=['Country/Region', 'Date'])
# filling na with 0
full_grouped = full_grouped.fillna(0)
# fixing data types
cols = ['New cases', 'New deaths', 'New recovered']
full_grouped[cols] = full_grouped[cols].astype('int')
#
full_grouped['New cases'] = full_grouped['New cases'].apply(lambda x: 0 if x<0 else x)

full_grouped.to_csv('COVID-19-time-series-clean-complete.csv')