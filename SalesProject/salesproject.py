# url="https://raw.githubusercontent.com/5225prachi/Sales_Prediction/refs/heads/main/index.csv"

#Sales Prediction Using Machine Learning (Real Dataset)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("Welcome to Sales Prediction Project")

df=pd.read_csv("https://raw.githubusercontent.com/5225prachi/Sales_Prediction/refs/heads/main/index.csv");

print(df.info())
print(df.describe())
print(df.head(5))
print(df.tail(5))

rows = df.shape[0]
columns = df.shape[1]

print("Row : ",rows)
print("Columns : ",columns)

print("SHAPE : ",df.shape)

print("Is Null : ",df.isnull())
print("Is Null Sum : ",df.isnull().sum()) # Card - 89

#check  for duplicate data
print("Duplicate Data :: ",df.duplicated())
print("Duplicate Data Sum:: ",df.duplicated().sum())

#Drop duplicate data
dpdata=df.drop_duplicates(inplace=True)
print("Drop duplicate data-",dpdata)


#Correlation Analysis
correlation = df.corr(numeric_only=True)
print("Correlation Analysis ",correlation)

#Histogram
import matplotlib.pyplot as plt

# df["money"].hist(bins=10)

# plt.title("Distribution of Sales")
# plt.xlabel("Sales")
# plt.ylabel("Frequency")
# plt.show()

df["coffee_name"].hist(bins=10)

plt.title("Distribution of Coffee Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["coffee_name"], df["money"])

plt.xlabel("Coffee")
plt.ylabel("Sales")
plt.title("Coffee vs Sales")

plt.show()

#Data Visualization
#Scatter Plot
plt.figure(figsize=(8,6))

plt.scatter(df["coffee_name"], df["date"])

plt.title("Daily Sales")

plt.xlabel("Coffee")

plt.ylabel("Interval ")

plt.show()