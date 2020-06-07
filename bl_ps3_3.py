#!/usr/bin/env python
import pandas as pd
file = input('Enter csv file name: ') 
try:
   test = open(file)
except:
    print('File cannot be opened, maybe you didn\'t add \'.csv\'?:', file)
    exit()
data=pd.read_csv(file,usecols=[0,1]) #read csv and store only first and second columns
data.columns=data.columns.str.strip().str.replace(' ', '_') #replace \s with _ in column name (annoying)
data['Diff_from_previous']=data.Water_Level.diff() #makes new column and uses the diff method to calculate differences in the 'water_level' column... default value is to calc diff between previous line.
sorted_data=data.sort_values(by=["Diff_from_previous"], ascending=False) #sort values by 'Diff' column, descending so first value is highest
ans1=sorted_data.iloc[[0]] #get top line = highest value
print("record of largest increase in water level observed:")
print(ans1.to_string(index=False)) #hide row number and just print info as string