import pandas as pd

import os

os.chdir('C:/Users/mikke/OneDrive - Syddansk Universitet/Data Science/10. Anvendt Maskinlæring/project/Assignment 2/mega ensemble')

df1 = pd.read_csv('pred (1) (1).csv') 
df2 = pd.read_csv('pred (2) (1).csv') 
df3 = pd.read_csv('pred (3) (1).csv') 

df1 = df1['Predicted']
df2 = df2['Predicted']
df3 = df3['Predicted']

df_final = pd.concat([df1,df2,df3], axis=1)

def calculate_majority(row):
  counts = pd.Series(row).value_counts()
  majority = counts.idxmax()
  return majority

df_final['majority'] = df_final.apply(calculate_majority, axis=1)

df_ensemble = pd.DataFrame({
    'Id': range(len(df_final)),
    'Predicted': df_final['majority'].values,
})

path_on_drive = 'C:/Users/mikke/OneDrive - Syddansk Universitet/Data Science/10. Anvendt Maskinlæring/project/Assignment 2/mega ensemble/pred_f.csv'
df_ensemble.to_csv(path_on_drive, index=False)
