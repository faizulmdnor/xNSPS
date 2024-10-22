import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

all_data = pd.read_csv('COVID-19-time-series-clean-complete.csv')

data = []

for row in all_data:
    if all_data['Country/Region'] == 'Malaysia':
        data.append(row)

print(data)

#data.drop(['Unnamed: 0'])

x = data['Date']
y1 = data['Confirmed']

y3 = data['Recovered']

plt.bar(x, y1, label='Confirmed', color='blue')

plt.bar(x, y3, label='Recovered', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Covid19: Malaysia')
plt.legend()
plt.show()
