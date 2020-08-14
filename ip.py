import pandas as pd
import collections
import numpy as np
df=pd.read_csv('hits.txt',delimiter='\t',names=['host','ip','page'])

df=df.groupby('ip').size().reset_index(name='count')
df=df.sort_values('count')
df=df.reset_index(drop=True)
print(df['ip'][len(df)-5:len(df)])