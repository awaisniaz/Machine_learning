import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

mu = 0.5
sigma = 0.1
np.random.seed(0)
X = np.random.normal(mu,sigma,(395,1))
Y = np.random.normal(mu*2,sigma*3,(395,1))
plt.scatter(X, Y, color='g')
plt.show()