from scipy.stats import pearsonr,spearmanr
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample Data
x = np.array([1, 2, 3, 4, 5])
xx=x.reshape(-1,1)
y = np.array([2, 4, 5, 8, 10])

#Pearson Correlation
r,_=pearsonr(x,y)
print("Pearson Correlation:\n",r)

#Spearman Correlation
rho,_=spearmanr(x,y)
print("Spearman Correlation:\n",rho)


# Fit Linear Regression
model = LinearRegression()
model.fit(xx, y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("R-Squared: ", model.score(x, y))