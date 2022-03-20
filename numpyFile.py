import numpy as np
import pandas as pd
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])


v = np.array([9,10])
w = np.array([11,12])

print(np.dot(v,w))
print(np.dot(x,v))
print(np.dot(x,y))

# scipy library
#
# from scipy.misc import imread, imsave, imresize
# img = imread('awais(2).jpg')

from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeRegressor

dataset = datasets.load_iris()
model =  DecisionTreeRegressor()
model.fit(dataset.data,dataset.target)
print(len(dataset.target))
expected =  dataset.target
predicted = model.predict(dataset.data)

print(metrics.classification_report(expected,predicted))
print(metrics.confusion_matrix(expected,predicted))


# Theano  Library

import theano
import theano.tensor as T
x = T.dmatrix('x')
s = 1/(1+T.exp(-x))
logistic = theano.function([x],s)
logistic([[0,1],[-1,-2]])

import tensorflow as tf
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])


result = tf.multiply(x1,x2)
sess = tf.Session()
print(sess.run(result))
sess.close()