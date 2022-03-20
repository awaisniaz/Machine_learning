import pandas as pd
import  scipy
import numpy

from sklearn.preprocessing import MinMaxScaler

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataFrame = pd.read_csv(url,names=names)
array = dataFrame.values
print(array)