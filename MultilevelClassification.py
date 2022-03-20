# Decision tree is best for Multilevel Classification
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

iris = datasets.load_iris()
X = iris.data
Y = iris.target


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=0)
from sklearn.tree import DecisionTreeClassifier

Dtree = DecisionTreeClassifier(max_depth=2).fit(X_train,Y_train)
prediction = Dtree.predict(X_test)

cm = confusion_matrix(prediction,Y_test)

print(cm)



