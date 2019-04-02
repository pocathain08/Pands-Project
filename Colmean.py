#Peadar O Cathain 02/04/2019
#This program will calculate the mean for each column

import numpy as ny

#Read the date file into an array
data = ny.genfromtxt('Iris dataset.csv', delimiter=',')


firstcol = data[1:,0]
seccol = data[2:,0]
#print (firstcol) testing the correct col returned
meanfirstcol = ny.mean(data[1:,0])
meanseccol = ny.mean(data[2:,0])
meanthicol = ny.mean(data[3:,0])
meanfoucol = ny.mean(data[4:,0])

print("The Mean of the first column is: ", meanfirstcol,
"The Mean of the second column is: ", meanseccol,
"The Mean of the third column is: ", meanthicol,
"The Mean of the fourth column is: ", meanfoucol,)
