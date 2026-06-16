#Exploratory Data Analysis (EDA)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load Titanic dataset
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
#Check Dataset
print("Dataset :",df)

#Inspect Data
print("Info : ",df.info()) #Able to see missing values
print("Describe : ",df.describe())

#Handle missing value
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Cabin"]=df["Cabin"].fillna("Unknown")
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
print("Info : ",df.info()) #Able to see missing values

#Remove Duplicates
df = df.drop_duplicates()
print("Info : ",df.info()) #Able to see duplicate values

# Filter data: Passengers in first class
first_class = df[df["Pclass"] == 1]
print("First Class Passengers: \n", first_class.head())

# Bar Chart: Survival rate by class
# survival_by_class = df.groupby("Pclass")["Survived"].mean()
# survival_by_class.plot(kind="bar", color="skyblue")
# plt.title("Survival Rate by class")
# plt.ylabel("Survival Rate")
# plt.show()

# Histogram: Age distribution
# sns.histplot(df["Age"], kde=True, bins=20, color="purple")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# Scatter Plot: Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()