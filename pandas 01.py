import pandas as pd
import numpy as np
from formatting import AnsiFontColors

fpath = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/'
fname = "UserDetails.csv"
filename = fpath+fname
print(filename)

# read csv data
data = pd.read_csv(filename)
print(data.head(10))
print(data.columns)

print