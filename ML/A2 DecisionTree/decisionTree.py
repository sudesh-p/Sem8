import numpy as np
import pandas as pd


dataset = pd.read_csv("data.csv")
X = dataset.iloc[:,:-1]
y = dataset.iloc[:,5].values

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()

X = X.apply(LabelEncoder().fit_transform)
print X

from sklearn.tree import DecisionTreeClassifier as NirnayJhaad
regressor = NirnayJhaad()
regressor.fit(X.iloc[:,1:5], y)

X_in = np.array([1,1,0,0])
y_pred = regressor.predict([X_in])
print "Prediction : ", y_pred


from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(regressor, out_file = dot_data, filled = True, rounded = True, special_characters = True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')
