import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("DataTable.csv")
x = data.iloc[:,:-1]
y = data.iloc[:,5]
x = x.apply(LabelEncoder().fit_transform)
print(x)
x_in = [1,1,0,0]
model = DecisionTreeClassifier()
model.fit(x.iloc[:,1:5].values,y.values)
print() #Empty Line
print("Model prediction for "+str(x_in)+" is ", model.predict([x_in]))
print() #Empty Line
plot_tree(model)
plt.show()