#This file, along with ipython will be used to test out the data 
#analysis hits from the Google. This is to discover what they do!
#Peadar O Cathain 

import numpy as ny

#Read the date file into an array
data = ny.genfromtxt('Iris dataset.csv', delimiter=',')
data.describe()

