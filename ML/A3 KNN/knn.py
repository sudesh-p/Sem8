import numpy as np
import pandas as pd

dataset = pd.read_csv("knncodes.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,2].values

from sklearn.neighbors import KNeighborsClassifier as KNC

classifier = KNC(n_neighbors = 3)
classifier.fit(X,y)

X_test = np.array([6,6])
y_pred = classifier.predict([X_test])
print('General KNN: ', y_pred)

classifier = KNC(n_neighbors = 3, weights = 'distance')
classifier.fit(X,y)

X_test = np.array([6,6])
y_pred = classifier.predict([X_test])
print('General KNN: ', y_pred)

