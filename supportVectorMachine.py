# Support Vector Machine is Efficient classificatiom method
from sklearn import datasets
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import  train_test_split

iris = datasets.load_iris()

X= iris.data
Y = iris.target
X_train,X_test,y_train,y_test = train_test_split(X,Y)
from sklearn.svm import SVC

vectorMachine = SVC(kernel='linear',C=1).fit(X_train, y_train)
svmprediction  = vectorMachine.predict(X_test)

accuracy = vectorMachine.score(X_test,y_test)
cm = confusion_matrix(y_test,svmprediction)
print(cm)