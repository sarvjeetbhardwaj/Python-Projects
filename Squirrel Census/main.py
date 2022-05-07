import pandas as pd

df=pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

df_1=df.groupby('Primary Fur Color').count()[['Age','Shift']]

df_1.to_csv('group_by_squirrel_count.csv')