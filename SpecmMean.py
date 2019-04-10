#This program will compare the mean of each species with the
#mean of the total dataset
#Peadar O Cathain


import numpy as ny
import pandas as pd


#Read the date file into an array
data = ny.genfromtxt('Iris dataset.csv', delimiter=',')

#sort the data set by species (use while true statement??)
print (data.head())
#col1 = data[1:,0]
#col2 = data[2:,0]
#print (firstcol) testing the correct col returned