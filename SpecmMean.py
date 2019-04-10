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
or (data[1:,4]) == ('setosa'):
    meancol1 = ny.mean(data[1:,0])
    meancol2 = ny.mean(data[1:,1])
    meancol3 = ny.mean(data[1:,2])
    meancol4 = ny.mean(data[1:,3])

print("The Mean of the first column is: ", meancol1,
"The Mean of the second column is: ", meancol2,
"The Mean of the third column is: ", meancol3,
"The Mean of the fourth column is: ", meancol4,)