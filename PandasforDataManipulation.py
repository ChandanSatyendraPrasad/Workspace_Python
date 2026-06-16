#Pandas for Data Manipulation
import pandas as pd
#Series Concept
data = [1,2,3,4,5]
print("data:", data)
s = pd.Series(data)
print("Series:", s)
#Custom Index
series_with_index = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print("Series with custom index:", series_with_index)

#DataFrame Concept
data = {'Name':['Alice','Bob','Charlie'],'Age':[25,30,35],'City':['New York','Los Angeles','Chicago']}
df = pd.DataFrame(data)
print("DataFrame:", df)
#Reading Data from CSV
df_csv = pd.read_csv('./customers-10000.csv')
print("DataFrame from CSV:", df_csv)

#Reading Data from Excel
df_excel = pd.read_excel("./employees.xlsx")
print("DataFrame from Excel:", df_excel)

df_csv.to_csv("./customer.csv", index=False)    
df_excel.to_excel("./employee.xlsx", index=False) 
print("DataFrame saved to CSV  successfully.",df_csv.to_csv("./customers-10000.csv", index=False))
print("DataFrame saved to Excel successfully.",df_excel.to_excel("./employees.xlsx", index=False))
print("DataFrame from CSV:", df_csv.head())
print("DataFrame from Excel:", df_excel.head())
print("Info for df_csv:")
print(df_csv.info())
print("Info for df_excel:")
print(df_excel.info())

#Summary statistics
print("Summary statistics for df_csv:")
print(df_csv.describe())
print("Summary statistics for df_excel:")
print(df_excel.describe())

#Accessing specific rows

print("Tail of df_csv:")
print(df_csv.tail(3))
print("Tail of df_excel:")
print(df_excel.tail(3))

#Selecting specific columns
print("Selecting 'First Name' and 'City' columns from df_csv:")    
print(df_csv[['First Name', 'City']])

print("Selecting 'First Name' and 'Salary' columns from df_excel:")
print(df_excel[['First Name', 'Salary']])

print("Selecting rows where Country = 'Zimbabwe' in df_csv:")
print(df_csv[df_csv['Country'] == 'Zimbabwe'])

print("Selecting rows where Salary > 50000 in df_excel:")
print(df_excel[df_excel['Salary'] > 50000])


#Selecting rows with multiple conditions
print("Selecting rows where Country = 'Zimbabwe' and City ='Barrettview' in df_csv:")
print(df_csv[(df_csv['Country'] == 'Zimbabwe') & (df_csv['City'] == 'Barrettview')])

print("Selecting rows where Salary > 110000 and Gender = 'Male' in df_excel:")
print(df_excel[(df_excel['Salary'] > 110000) & (df_excel['Gender'] == 'Male')])

#Value counts
print("Value counts for 'Country' column in df_csv:")
print(df_csv['Country'].value_counts())
print("Value counts for 'Location' column in df_excel:")
print(df_excel['Location'].value_counts())

#Unique values
print("Unique values in 'City' column of df_csv:")
print(df_csv['City'].unique())
print("Unique values in 'Location' column of df_excel:")
print(df_excel['Location'].unique())

print(df_csv.iloc[0])  # First row
print(df_csv.iloc[1:4])  # Rows 1 to 3
print(df_csv.loc[df_csv['Country'] == 'Zimbabwe'])  # Rows where Country is Zimbabwe
print(df_excel.iloc[0])  # First row    
print(df_excel.iloc[1:4])  # Rows 1 to 3
