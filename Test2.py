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

data = pd.read_csv('Iris dataset.csv')

print (data.head())
print (data.tail())
 
print (data.info())
print (data.describe())

#print (data['Species'].value_counts())





