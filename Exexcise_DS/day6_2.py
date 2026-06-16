import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print("Dataset",df)
print("Info",df.info())

del df['species']
# Calculate correlation matrix
correlation_matrix=df.corr()

# plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
