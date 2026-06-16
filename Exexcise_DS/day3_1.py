import pandas as pd
#Load dataset from CSV file
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(path)
print("DataFrame from CSV:", df)
#describe the dataset
print("Summary statistics for df:")
print(df.describe())
#Accessing specific rows
print("Tail of df:")
print(df.tail(3))
#Selecting specific columns
print("Selecting 'species' and 'sepal_length' columns from df:")
print(df[['species', 'sepal_length']])

#Filtering rows based on conditions
print("Selecting rows where species = 'setosa' in df:")
print(df[df['species'] == 'setosa'])

print("Selecting rows where sepal_length > 6.0 in df:")
print(df[df['sepal_length'] > 6.0])

print("Selecting rows where petal_length > 5.0 in df:")
print(df[df['petal_length'] > 5.0])

print("Selecting rows where species = 'virginica' and sepal_width > 3.0 in df:")
print(df[(df['species'] == 'virginica') & (df['sepal_width'] > 3.0)])

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered Rows: \n", filtered_rows)