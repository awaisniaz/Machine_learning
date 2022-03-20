# imbalance techniques
# Smote
# Near Miss Algorithm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,classification_report

data = pd.read_csv('creditcard.csv')
print(data.info())
data['normAmount'] = StandardScaler().fit_transform(np.array(data['Amount']))
data = data.drop(['Time','Amount'],axis=1)
data['Class'].value_counts()

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X)
