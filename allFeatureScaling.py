# All Feature Scaling and Normalization

# Normalization (Range (0,1) , (-1,1))
# Standardization (mean = 0 ,variance = 1)

# Min Max Scaler
# Standard Scaler
# Max Abs Scaler
# Robust Scaler
# Quantile Transform Scaler
# Power Transform Scaler
# Unit Vector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'WEIGHT': [15, 18, 12,10],
                   'PRICE': [1,3,2,5]},
                   index = ['Orange','Apple','Banana','Grape'])
print(df)

# Min Max Scaler
# Is getting used when standard deviation is small and distribution is small
# Scaler is very sensitive

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df1 = pd.DataFrame(scaler.fit_transform(df),columns=['WEIGHT','PRICE'],
                   index=['Orange','Apple','Banana','Grape'])
print(df1)



# Standard Scaler
# When data is normally distributed  mean  = 0 , variance = 1

from sklearn.preprocessing import StandardScaler
standard = StandardScaler()
df2 = pd.DataFrame(standard.fit_transform(df),
                   columns=['WEIGHT','PRICE'],
                   index = ['Orange','Apple','Banana','Grape'])

print(df2)


# Max Abs Scaler
# Scaler maximum absolute value
# Sensitive to Outlier
from sklearn.preprocessing import  MaxAbsScaler
maxAbs = MaxAbsScaler()

df3 = pd.DataFrame(maxAbs.fit_transform(df),
                   columns=['WEIGHT','PRICE'],
                   index = ['Orange','Apple','Banana','Grape'])
print(df3)

#Robust Scaler
# Is not work well when outlier is present in dataset
from sklearn.preprocessing import RobustScaler

scalerRobust = RobustScaler()
df4 = pd.DataFrame(scalerRobust.fit_transform(df),
                   columns=['WEIGHT','PRICE'],
                   index = ['Orange','Apple','Banana','Grape'])
print(df4)


#Quantile Transformer Scaler
# Follow uniform or normal Distirbution


