from sklearn.datasets import make_blobs,make_moons,make_circles
from matplotlib import pyplot  as plt
from matplotlib import  style

style.use('fivethirtyeight')

# X,Y = make_blobs(n_samples=100,centers=3,cluster_std=1,n_features=2)
# X,Y = make_moons(n_samples = 100, noise=0.02)
X,Y = make_circles(n_samples=100,noise=0.02)
plt.scatter(X[:,0],X[:,1],s = 40,color='r')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
plt.clf()