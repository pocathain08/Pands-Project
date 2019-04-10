#This notebook demos Python data visualizations on the Iris dataset
# Ref :https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
#peadar o cathain 08 Apr 2019

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set(color_codes=True)

#%matplotlib inline
#%pylab inline
#matplotlib inline

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#reads in the CSV file as a pandas dataframe
df = pd.read_csv('Iris dataset.csv')
#Prints the first five entries 
print (data.head())
#Prints the first five entries
print (data.tail())
 
print (data.info())
#Metadata of the dataframe
print (data.describe())
#gives the mean, max, min of the dataframe.

#print (data['Species'].value_counts()) Not working
#if 'Id' in data.columns:
 # data.__delitem__('Id') #???
#print (data.head())

print (data['Species'].unique()) Not working


print (df.groupby('species').size())

df.hist(figsize=(10,5))
plt.show()















