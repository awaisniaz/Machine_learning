# Feature Distance Measure
# Euclidean Distance
# Manhattan Distance
# Minkowski Distance


# Feature Scaling Techniques
# Min Max Normalization (Range Between ( 0 -------------- 1))
# Standardization (0 mean and 1 variance)

import pandas as pd
from sklearn import preprocessing
data = pd.read_csv('data.csv')
print(data.head(3))
x = data.iloc[:,1:3].values
# Min Max Scaler
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
x_after_scaling = min_max_scaler.fit_transform(x)
print(x_after_scaling)

# Standardization
from sklearn.preprocessing import StandardScaler

standard = StandardScaler()
x_after_standard = standard.fit_transform(x)
print(x_after_standard)

