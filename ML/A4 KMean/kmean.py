import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 X=[[0.1,0.6],[0.15,0.71],[0.08,0.9],[0.16,0.85],[0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]]

centers=np.array([[0.1,0.6],[0.3,0.2]])
print('Initial Centroids:\n',centers),centers

from sklearn.cluster import KMeans as KSarasari
model=KSarasari(n_clusters=2,init=centers,n_init=1)
model.fit(X)

print('Labels:',model.labels_)
print('P6 belongs to cluster',model.label_[5])
print(np.count_nonzero(model.labels_==1))
print('New Centroids:/n',model.cluster_centers_)

centers


plt.plot(model.labels_,'*')
plt.show()
