#!/usr/bin/env python
import csv                              #bring in csv reader
file = input('Enter csv file name: ')   #ask user for file name
try:                                    #try to open user file
    with open(file, 'rt') as csv_file:  
        next(csv_file)                  #skip header row!
        reader = csv.reader(csv_file, delimiter=",")    #file handle = 'reader'
        dates=[]                        #create empty lists for dates and levels
        levels=[]
        for row in reader:
            dates.append(row[0])        #fill the empty lists with the values from the csv 
            levels.append(row[1])       #this makes a list of water levels, but they are still strings 
        nums=[]                         #make a new empty list called 'nums' where we will convert strings to numbers
        for i in levels:                #conversion loop
            try:
                nums.append(float(i))   #convert strings into floats.. unless it's empty
            except:
                nums.append(float(0))   #...replaces empty values with number 0 
except:
    print('File cannot be opened, maybe you didn\'t add \'.csv\'?:', file)
    exit()

                                        #now, calculate highest value
val=0                                   #set a starting point
for i in nums:
   if i>val: val=i                      #loop that replaces 'val' with any higher number encountered
idx=nums.index(val)                     #find the index that corresponds with val using the 'list.index' method
day=dates[idx]                          #report the date using the same index, using list[index]
print("The highest water level,",val,",","was observed on", day) #answer
