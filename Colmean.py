#Peadar O Cathain 02/04/2019
#This program will calculate the mean for each column

import numpy as ny

#Read the date file into an array
data = ny.genfromtxt('Iris dataset.csv', delimiter=',')


#col1 = data[1:,0]
#col2 = data[2:,0]
#print (firstcol) testing the correct col returned
meancol1 = ny.mean(data[1:,0])
meancol2 = ny.mean(data[1:,1])
meancol3 = ny.mean(data[1:,2])
meancol4 = ny.mean(data[1:,3])

print("The Mean of the first column is: ", meancol1,
"The Mean of the second column is: ", meancol2,
"The Mean of the third column is: ", meancol3,
"The Mean of the fourth column is: ", meancol4,)
