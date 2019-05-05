#This is a model that predicts the accuracy of using the features (Sepal length/width,
#petal length/width) of the data to predict the target (Species).
#Peadar O Cathain 05 May 2019




from  sklearn import  datasets
iris=datasets.load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)
from sklearn import tree
classifier=tree.DecisionTreeClassifier()
classifier.fit(x_train,y_train)
predictions=classifier.predict(x_test)
from sklearn.metrics import accuracy_score
print ("Given the features of the data, the accuracy of predicting the Species is:")
print(accuracy_score(y_test,predictions))