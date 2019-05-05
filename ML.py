#This will run some scikit learning programs.
#This program is heavily based on Ref 2 below and is designed to confirm if I get the Traceback
#File "C:\Users\35386\Anaconda3\lib\site-packages\matplotlib\pyplot.py", line 8
    #The object-oriented API is recommended for more complex plots.
#Ref: Introduction to ML with Python by Andreas C. Müller & Sarah Guido
#Peadar O Cathain 05 May 2019

#import sys print ("Python version: {}".format(sys.version)) 
#import pandas as pd #print ("pandas version: {}".format(pd.__version__)) 
#import matplotlib as plt #print ("matplotlib version: {}".format(matplotlib.__version__)) 
#import numpy as np #print ("NumPy version: {}".format(np.__version__)) 
#import scipy as sp #print ("SciPy version: {}".format(sp.__version__)) 
#import IPython print ("IPython version: {}".format(IPython.__version__)) 
#import sklearn #print ("scikit-learn version: {}".format(sklearn.__version__)) 

# Ref2:https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html#sphx-glr-auto-examples-datasets-plot-iris-dataset-py

import matplotlib.pyplot as plt
#File "C:\Users\35386\Anaconda3\lib\site-packages\matplotlib\pyplot.py", line 8
    #The object-oriented API is recommended for more complex plots.
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()
