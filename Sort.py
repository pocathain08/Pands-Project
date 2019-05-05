#This program will sort date by species type for comparison
#Objective is to create a species specific file
#Ref: pandas: pwoerful Python data analysis toolkit by Wes McKinney & PyData Development Team, 31 Mar 2019
#Peadar O Cathain 05 Apr 2019

import numpy as ny
import pandas as pd

data = pd.read_csv("Iris dataset.csv")

print (type(data))

print (data.head(3))
print (data.index)

#This program will look at the individual species and compare species avarages to the total averages. 
#This could determine which of the species is most typical.
#It does so by taking a one dimentional series from the dataframe.
data1=data[data['species'] == 'setosa']
data2=data[data['species'] == 'versicolor']
data3=data[data['species'] == 'virginica']
#check data to ensure it is sliced by species
print (data1.describe())
print (data1.head(3))
print (data2.describe())
print (data2.head(3))
print (data3.describe())
print (data3.head(3))

dfmean= (data.mean())
df1mean= (data1.mean())
df2mean= (data2.mean())
df3mean= (data3.mean())

print (df1mean)
print (type(df1mean))
#print (df1mean.loc[1,1])
print (df1mean.ndim)

frames = [dfmean, df1mean, df2mean, df3mean]
Indices = ('Iris', 'Setosa', 'Versicolor', 'Virginica')
Means=pd.DataFrame(frames, index = Indices)
#result = pd.concat(frames)
print (Means)



