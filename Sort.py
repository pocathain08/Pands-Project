#This program will sort date by species type for comparison
#Objective is to create a species specific file
#Peadar O Cathain 05 Apr 2019

import numpy as ny
import pandas as ps


#Read the date file into an array
data = ny.genfromtxt('Iris dataset.csv', delimiter=',')
#Index the five columns
#df=pd.data(np.random.randn(150,5) columns=['A', 'B', 'C', 'D', 'E'])
data.target_names

