#!/usr/bin/env python
import pandas as pd
file = input('Enter csv file name: ') 
try:
   test = open(file)
except:
    print('File cannot be opened, maybe you didn\'t add \'.csv\'?:', file)
    exit()
def read():
    try:
        data=pd.read_csv(file,usecols=[0,1]) #get only first and second columns
        data.columns=data.columns.str.strip() #removes white space from column to allow sort
        sorted_data=data.sort_values(by=["Water Level"], ascending=False) #sorts by col
        ans1=sorted_data.iloc[[0]] #get top line = highest value
        print("record of highest water level observed:")
        print(ans1.to_string(index=False)) #hide row number and just print water level and date
    except:
        print('problems reading file')
        exit()
read()