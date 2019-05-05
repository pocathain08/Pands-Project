#This is a model that predicts the accuracy of using the features (Sepal length/width,
#petal length/width) of the data to predict the target (Species).
#Ref:https://medium.com/@jebaseelanravi96/machine-learning-iris-classification-33aa18a4a983
#Peadar O Cathain 05 May 2019




from  sklearn import  datasets
#Create the dataset
iris=datasets.load_iris()
#Assign the data, x = features y=targets
x=iris.data
y=iris.target
#Split the dataset into training and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)
#x_train contains the training features
#x_test contains the testing features
#y_train contains the training label
#y_test contains the testing labels

from sklearn import tree
classifier=tree.DecisionTreeClassifier()
#train the model with fit function
classifier.fit(x_train,y_train)
#Make predictions with the predict function
predictions=classifier.predict(x_test)
#The predictions can be matched with the expected output to measure the accuracy value
from sklearn.metrics import accuracy_score
print ("Given the features of the data, the accuracy of predicting the Species is:")
print(accuracy_score(y_test,predictions))