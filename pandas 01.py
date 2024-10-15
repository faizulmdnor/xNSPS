import pandas as pd
import numpy as np

fpath = 'E:/X-NSPS/Python - Scripting/pythonProject/xNSPS/'
fname = "2011_2021_statistik_tangkapan_pesalah_rasuah.csv"
filename = fpath+fname
print(filename)

# read csv data
data = pd.read_csv(filename)
print(data.head(10))
print(data)