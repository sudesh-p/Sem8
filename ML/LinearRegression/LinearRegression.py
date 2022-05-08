import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("LR.csv")
x = data.iloc[:,:-1].values
y = data.iloc[:,1].values
model = LinearRegression()
model.fit(x,y)
eq = str("y = ") + str(model.coef_[0]) +  str("* x +") + str(model.intercept_)
print(eq)
print()
plt.plot(x,y,"o")
plt.plot(x,model.predict(x))
plt.show()