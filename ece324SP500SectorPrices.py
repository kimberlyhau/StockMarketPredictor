import pandas as pd
import datetime as dt
import numpy as np
import os

#Read Path and pick out excel files
files = os.listdir("ECE324 Interim Report/Excel Files")
xls = [f for f in files if f[-3:] == 'xls']

#For every excel file, read in file. Store in master list
dfList = []
for f in xls:
    data = pd.read_excel('ECE324 Interim Report/Excel Files/'+str(f), 'Performance Graph',skiprows= (range(1259,1278)),header = 6, usecols="A:B")
    dfList += [data]

#Combine all prices in one dataframe, remove duplicate date columns
df = pd.concat(dfList, axis = 1)
df = df.loc[:,~df.columns.duplicated()]

#start the dataframe at the desired date
starteDate = dt.datetime(2019,1,2, 0, 0, 0)
index = df[df['Effective date '] == starteDate].index
df = df.iloc[index[0]:]

#resret index
df  = df.set_index(['Effective date '], drop = True)

#save data to text file
df.to_csv("ECE324 Interim Report/Excel Files/SP500Data.txt")