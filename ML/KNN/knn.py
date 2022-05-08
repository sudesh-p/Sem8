#import the packages
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

dataset=pd.read_csv("knncodes.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,2].values
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,y)
X_test=np.array([6,1])
y_pred=classifier.predict([X_test])
print('General KNN:',y_pred)
plt.plot(X,y,"o")
plt.plot([X_test],y_pred,"*")
plt.show()
classifier=KNeighborsClassifier(n_neighbors=3,weights='distance')
classifier.fit(X,y)
X_test=np.array([6,6])
y_pred=classifier.predict([X_test])
print('Distance Weighted KNN:',y_pred)
plt.plot(X,y,"o")
plt.plot([X_test],y_pred,"*")
plt.show()
classifier=KNeighborsClassifier(n_neighbors=3,weights='uniform')
classifier.fit(X,y)
X_test=np.array([6,6])
y_pred=classifier.predict([X_test])
print('Distance Weighted KNN:',y_pred)
plt.plot(X,y,"o")
plt.plot([X_test],y_pred,"*")
plt.show()

# Import np pd Kneighbors without u
# read dataset iloc with , to x and y with values
# define model with 3 neighbors define xtest and predict
# repeat same with distance as well