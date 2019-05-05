#This Program will be used to plot the data obtained from Sort.py, using that script.
#Referance: pandas: powerful Python data analysis toolkit by Wes McKinney & PyData Development Team, 31 Mar 2019
#Peadar O Cathain 03 May 2019


import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
#import matplotlib.pyplot as plt
#When I import matplotlib, I get the following 
    #Traceback File "C:\Users\35386\Anaconda3\lib\site-packages\matplotlib\pyplot.py", line 8
        #The object-oriented API is recommended for more complex plots.

data = pd.read_csv("Iris dataset.csv")
print (data.info())
print(data['species'].value_counts())

print("Target names: {}".format(data['target_names']))


print("Keys of iris_dataset: \n{}".format(data.keys()))


data1=data[data['species'] == 'setosa']
data2=data[data['species'] == 'versicolor']
data3=data[data['species'] == 'virginica']

dfmean= (data.mean())
df1mean= (data1.mean())
df2mean= (data2.mean())
df3mean= (data3.mean())

frames = [dfmean, df1mean, df2mean, df3mean]
Indices = ('Iris', 'Setosa', 'Versicolor', 'Virginica')
Means=pd.DataFrame(frames, index = Indices)
#result = pd.concat(frames)
print (Means)
