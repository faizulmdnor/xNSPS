import pandas as pd
import numpy as np

data = {'name':['faizul', 'amirul', 'sarah', 'sharirah', 'tacha'],
        'asal':['penang', 'kedah', 'kedah', 'selangor', 'kedah'],
        'umur': [45, 27, 26, 25, 25]}

df = pd.DataFrame(data)

print(df)

name = ['faizul', 'amirul', 'sarah', 'sharirah', 'tacha']
umur = [45, 27, 26, 25, 25]
asal = ['penang', 'kedah', np.nan, 'selangor', 'kedah']

df2 = pd.DataFrame(columns=['name', 'umur', 'asal'])
df2['name'] = name
df2['asal'] = asal
df2['umur'] = umur

print(df2)
