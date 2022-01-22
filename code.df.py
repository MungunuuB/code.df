# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:44:13 2022

@author: Dell
"""

import pandas as pd
import numpy as np
column_names = ["a", "b", "c"]
df = pd.DataFrame(columns = column_names)
df2 = {'a': 'Vikram', 'b': 'Aruchamy', 'c': 'India'}
df = df.append(df2, ignore_index = True)
df.loc[1] = ['India', 'Shivam', 'Pandey']
df.loc[len(df)]= ['I', 'S', 'Mguu']
df.rename(columns = {'a': 'Year', 'b': 'Income'},inplace = True)
df1 = df[["Year", "Income"]]       
 df = df.replace('S', np.nan)
df.dropna()
df.dropna(how='all')
df.dropna(how='any')
df.dropna(axis=1)
df.fillna(method='ffill')
df.fillna(method='bfill')
