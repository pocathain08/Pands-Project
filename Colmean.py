#Peadar O Cathain 02/04/2019
#This program will calculate the mean for each column using numpy

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

print("The Mean of the first column is: ", meancol1)
print("The Mean of the second column is: ", meancol2)
print("The Mean of the third column is: ", meancol3)
print("The Mean of the fourth column is: ", meancol4)

#Peadar O Cathain 05/05/2019
#This program will give a full description of the data using pandas
import pandas as pd

data = pd.read_csv("Iris dataset.csv")

print ("\nThis data type is:", type(data))
#Number of rows and columns 
print("\nThe number of rows and columns in the DataFrame is:", (data.shape), "\n")
#use "\n" the make the data more presentable and easier to read in the README file
#Number of dimensions in dataframe
print ("The dimension of the DataFrame is:") 
print((data.ndim), "\n")
#The types of each column
print("The data types are as follows:") 
print(data.dtypes)
#Description of the data, basic stats on cols
print ("\nThe following is a brief statistical description of the DataFrame:")
print(data.describe())


