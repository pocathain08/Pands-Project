# This program will give the reader an idea of what the data
# looks like as well as introducing some Machine learning terminology
# It will primarily use Pandas
#Ref:Python tutorial for students Machine Learning Course_Holzinger
#Peadar O Cathain 01 May 2019

import numpy as ny
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(iris.data)
df.columns = ["sepal_l", "sepal_w", "petal_l", "petal_w"]
#

print (df.head (3)) 
#Insret a column to include the species name
df["species"] = iris.target
df.loc[df.species == 0, "species"]= "Setosa"
df.loc[df.species == 1, "species"] = "Versicolor"
df.loc[df.species ==2, "species"] = "Virginicia"
#check to confirm species names.
print (df.iloc[0])
print (df.iloc [50])
print (df.iloc[149])
print (df.head (3))

df.sort_values(by = "species")
print (df.iloc[48:52])

from pandas.tools.plotting import pandas.plotting.scatter_matrix #as scatter_matrix
scatter_matrix(df, diagonal="kde")

#plt.show()




