# Importing Libraries:
import pandas as pd
import numpy as np
from formatting import AnsiEffect, AnsiFontColors, AnsiBackColors

name = input('Name: ')
print(f'Hello, my name is {name}')

# Creating a 1D array
array1 = np.array([1, 2, 3, 4])
print(array1)

# Creating a 2D array
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array2)

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# Selecting a column
print(df['Name'])

# Filtering rows
print(df[df['Age'] > 30])

# Adding a new column
df['Salary'] = [70000, 80000, 90000]
print(df)
