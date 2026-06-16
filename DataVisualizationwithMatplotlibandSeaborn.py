# Data Visualization with Matplotlib and Seaborn
import pandas as pd
import matplotlib.pyplot as plt

# Load employee data from Excel
employee_file = 'employee.xlsx'
df = pd.read_excel(employee_file)
print('Data loaded successfully from employee.xlsx')
print(df.head())  # Display the first few rows of the DataFrame
print('DataFrame columns:', df.columns)  # Print the column names to verify
#Find the missing value in the data for Loccation column
missing_location_count = df['Location'].isnull().sum()
print(f'Missing values in Location column: {missing_location_count}')
missing_salary_count = df['Salary'].isnull().sum()
print(f'Missing values in Salary column: {missing_salary_count}')
# Plot employee counts by location and salary distribution in two views
# if the respective columns exist
for column in ['Location', 'Salary']:
    if column in df.columns:
        print(f'Column "{column}" exists in the DataFrame.')
    else:
        print(f'Column "{column}" does NOT exist in the DataFrame.')
if 'Location' in df.columns:
    location_counts = df['Location'].value_counts().sort_values(ascending=False)
    location_counts.plot(kind='bar', color='skyblue')
    plt.title('Employees by Location')
    plt.xlabel('Location')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
elif 'Salary' in df.columns:
    plt.hist(df['Salary'].dropna(), bins=10, color='skyblue', edgecolor='black')
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
else:
    print('Loaded employee.xlsx with columns:', list(df.columns)) 
