#Data Aggregation and Grouping in Pandas
import pandas as pd
# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Group by 'Category' and calculate the sum of 'Value'
grouped_sum = df.groupby('Category')['Value'].sum()
print("\nSum of Values by Category:")
print(grouped_sum)
# Group by 'Category' and calculate the mean of 'Value'
grouped_mean = df.groupby('Category')['Value'].mean()
print("\nMean of Values by Category:")
print(grouped_mean)

cust=pd.read_csv('./customer.csv')
print("\nCustomer DataFrame:")
print(cust.describe())
print("\nCustomer DataFrame Info:")
print(cust.info())
# Group by 'Country' 
grouped_country = cust.groupby('Country').size()
print("\nNumber of Customers by Country:")
print(grouped_country)

employee=pd.read_excel('./employee.xlsx')
employee_dataframe = pd.DataFrame(employee)
print("\nEmployee DataFrame:")
print(employee_dataframe.describe())
print("\nEmployee DataFrame Info:")
print(employee_dataframe.info())
# Group by a generic column
generic_groupped = employee_dataframe.groupby("Salary").size()
print("\nGeneric Grouped DataFrame:")
print(generic_groupped)



#pivot_table
pivot_table = pd.pivot_table(employee_dataframe, values='Salary', index='Location', aggfunc='mean')
print("\nPivot Table (Mean Salary by Location):")
print(pivot_table)

#mean, median, mode
mean_salary = employee_dataframe['Salary'].mean()
median_salary = employee_dataframe['Salary'].median()
mode_salary = employee_dataframe['Salary'].mode().iloc[0]
print("\nMean Salary:", mean_salary)
print("Median Salary:", median_salary)  
print("Mode Salary:", mode_salary)  