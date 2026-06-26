import numpy as np  # numerical computing library, aliased as np
import pandas as pd  # data manipulation library, aliased as pd
import matplotlib.pyplot as plt  # plotting library, aliased as plt
from sklearn.datasets import fetch_california_housing  # function to load the California housing dataset
from sklearn.preprocessing import PolynomialFeatures  # transformer to generate polynomial and interaction features
from sklearn.linear_model import LinearRegression  # ordinary least squares regression model
from sklearn.metrics import mean_squared_error  # metric to evaluate regression model performance
from sklearn.linear_model import Ridge, Lasso  # regularized linear regression models
from sklearn.model_selection import train_test_split  # utility to split data into train/test sets

# Load the California Housing dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Select feature (Median Income) and target (Median House Value)
X = df[['MedInc']]  # feature matrix containing the Median Income column
y = df[['MedHouseVal']]  # target vector containing the Median House Value column
# Transform feature to polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)  # create transformer for degree-2 polynomials without bias term
X_poly = poly.fit_transform(X)  # fit transformer to X and transform into polynomial feature matrix

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)  # 80/20 split with fixed seed

# # Ridge Regression
# ridge_model = Ridge(alpha=1)  # initialize Ridge regression with regularization strength alpha=1
# ridge_model.fit(X_train, y_train)  # fit Ridge model on training data
# ridge_predictions = ridge_model.predict(X_test)  # predict targets for test set using Ridge


# # Lasso Regression
# lasso_model = Lasso(alpha=0.1)  # initialize Lasso regression with alpha=0.1
# lasso_model.fit(X_train, y_train)  # fit Lasso model on training data
# lasso_predictions = lasso_model.predict(X_test)  # predict targets for test set using Lasso

# # Evaluate Ridge Regression
# ridge_mse = mean_squared_error(y_test, ridge_predictions)  # compute MSE for Ridge predictions
# print("Ridge Regression MSE:", ridge_mse)  # print Ridge MSE


# # Evaluate Lasso Regression
# lasso_mse = mean_squared_error(y_test, lasso_predictions)  # compute MSE for Lasso predictions
# print("Lasso Regression MSE:", lasso_mse)  # print Lasso MSE

# # Visualize Ridge vs Lasso predictions
# plt.figure(figsize=(10,6))  # create a new figure with specified size
# plt.scatter(X_test[:, 0], y_test, color="blue", label="Actual Data", alpha=0.5)  # plot actual target vs first feature
# plt.scatter(X_test[:, 0], ridge_predictions, color="green", label="Ridge Predictions", alpha=0.5)  # plot Ridge predictions
# plt.scatter(X_test[:, 0], lasso_predictions, color="orange", label="Lasso Predictions", alpha=0.5)  # plot Lasso predictions
# plt.title("Ridge vs Lasso Regression")  # set plot title
# plt.xlabel("Median Income (Transformed)")  # set x-axis label
# plt.ylabel("Median House Value in California")  # set y-axis label
# plt.legend()  # show legend
# plt.show()  # display the plot

# Fit polynomial regression model
model = LinearRegression()  # initialize linear regression model
model.fit(X_poly, y)  # fit model on polynomial features and target values

# Make Predictions
y_pred = model.predict(X_poly)  # predict target values using the fitted model

# Plot actual vs predicted values
plt.figure(figsize=(10,6))  # create a new figure with specified dimensions
plt.scatter(X, y, color="blue", label="Actual Data", alpha=0.5)  # plot actual target values
plt.scatter(X, y_pred, color="red", label="Predicted Curve", alpha=0.5)  # plot predicted values
plt.title("Polynomial Regression")  # set the plot title
plt.xlabel("Median Income in California")  # set x-axis label
plt.ylabel("Median House Value in California")  # set y-axis label
plt.legend()  # display the legend
plt.show()  # display the plot

# Evaluate model performance
mse = mean_squared_error(y, y_pred)  # calculate mean squared error between actual and predicted values
print("Mean Squared Error (MSE): ", mse)  # print the MSE value