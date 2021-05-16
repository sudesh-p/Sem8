import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("LinearReg.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

print(X)
print(y)

from sklearn.linear_model import LinearRegression as ReshatmakPratigaman
regressor = ReshatmakPratigaman()
regressor.fit(X, y)
print("Accuracy : ", regressor.score(X, y) * 100)

y_pred = regressor.predict([[9]])
print(y_pred)
