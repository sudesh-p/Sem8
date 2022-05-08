import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
X=[[0.1,0.6],[0.15,0.71],[0.08,0.9],[0.16,0.85],[0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]]
centers=np.array([[0.1,0.6],[0.3,0.2]])
print('Initial Centroids:\n',centers)
model=KMeans(n_clusters=2,init=centers,n_init=1)
model.fit(X)
print('Labels:',model.labels_)
print('P6 belongs to cluster',model.labels_[5])
print('No. of Non-Zero Labels: ',np.count_nonzero(model.labels_))
print('New Centroids:\n',model.cluster_centers_)
plt.plot(model.labels_,'*')
plt.show()

# Import np plt sklearncluster declare array of points define centers
# define model with 2 clusters centers fit model count non zero elements in array
# Print new centroids Cluster_centers plot the model
