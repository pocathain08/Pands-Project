#This notebook demos Python data visualizations on the Iris dataset
# Ref :https://www.kaggle.com/benhamner/python-data-visualizations
#peadar o cathain 08 Apr 2019

#Import pandas, a data processing and CSV file I/O library
import pandas as pd
import numpy as ny

#Import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

# Load the Iris flower dataset, from C:\Users\35386\OneDrive\Desktop\Pands-Project\Iris dataset.csv.
#However no need to give full directory as file and program are in the same directory
iris = pd.read_csv("Iris dataset.csv") # the iris dataset is now a Pandas DataFrame

# Let's see what's in the iris data - Jupyter notebooks print the result of the last thing you do
##head=iris.head()
##print (head) #Prints the first 5 rows
##Ref https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris/
colors = ['red','green','blue'] # Dictionary classes -> colors
data = numpy.array(data, dtype="float") # Convert data to an array
M = (data-numpy.mean(data.T, axis=1)).T # Mean-center the data

# Find the matrix of principal components
[latent, coeff] = numpy.linalg.eig(numpy.cov(M)) 
coords = numpy.dot(coeff.T, M)   # Convert data to PC coordinates

fig, ax = matplotlib.pyplot.subplots() # Create matplotlib figure
for i in range(data.shape[0]): # Plot all the points
    ax.scatter(coords[0,i], coords[1,i], color=colors[labels[i]]
