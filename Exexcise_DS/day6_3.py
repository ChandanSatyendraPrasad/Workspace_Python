import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
#df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
df=pd.read_csv('cleaned_dataset.csv')
print("Dataset",df)
print("Info",df.info())

# Calculate correlation matrix
correlation_matrix=df.corr()

# plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
