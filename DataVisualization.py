# Data Visualization
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


import seaborn as sns
#Basic Plot
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.title("Basic Plot")
# plt.plot(x, y)
# plt.show()

#Line Plot
# plt.plot([1,2,3],[10,20,30],label="Trend",color="orange",linestyle="--",marker="X")
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.show()

#Bar Chart

# categories = ["A", "B", "C"]
# values = [10, 15, 7]
# plt.bar(categories, values, color="blue")
# plt.title("Bar Chart")
# plt.show()

# # Histogram
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(data, bins=4, color="green", edgecolor="black")
# plt.title("Histogram")
# plt.show()

# Scatter Plot
# x = [1, 2, 3, 4, 5]
# y = [10, 12, 25, 30, 45]
# plt.scatter(x, y, color="red")
# plt.title("Scatter Plot")
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")
# plt.legend(["Dataset 1"])
# plt.show()

# Load employee data from Excel
# employee_file = 'employee.xlsx'
# df = pd.read_excel(employee_file)
# print('Data loaded successfully from employee.xlsx')
# print(df.head())  # Display the first few rows of the DataFrame
# print('DataFrame columns:', df.columns)  # Print the column names to verify
# x=df['Salary']
# print(x)
# y=df['Location']
# print(y)
# plt.bar(x, y, color="red")
# plt.title("Locarion Vs Salary Plot")
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")
# plt.legend(["Dataset 1"])
# plt.show()

# data = np.random.rand(5, 5)
# print(data)
# sns.heatmap(data, annot=True, cmap="coolwarm")
# plt.title("HeatMap")
# plt.show()

employee_file = 'employee.xlsx'
df = pd.read_excel(employee_file)
sns.pairplot(df)
plt.title("Pair Plot")
plt.show()