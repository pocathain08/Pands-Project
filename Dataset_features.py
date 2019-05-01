# This program will give the reader an idea of what the data
# looks like as well as introducing some Machine learning terminology
# Ref: MAchine Learning Guide
#Peadar O Cathain 01 MAy 2019

import csv
import numpy
import pandas as pd


iris = pd.read_csv('Iris dataset.csv')

#iris=load_iris()
iris.keys()
iris.features_names
iris.target_names
iris.data.shape



