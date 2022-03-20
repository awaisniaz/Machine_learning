# One Hot Encoding
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
hotEncoding = OneHotEncoder()
data = pd.read_csv('data.csv')
print(data)
print(data['Country'].value_counts())

oneHot = pd.get_dummies(data,columns=['Country','Purchased'],drop_first=True)
print(oneHot)
