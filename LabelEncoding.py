import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
data = pd.read_csv('data.csv')
print(data)
data['Country'] = LabelEncoder().fit_transform(data['Country'])
data['Purchased'] = LabelEncoder().fit_transform(data['Purchased'])
data = data.dropna()
X = data.iloc[:,0:3]
X = StandardScaler().fit_transform(X)
print(X)


# Problem of Label Encoding is to give the priority of element
