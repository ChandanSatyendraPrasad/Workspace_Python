# Import pandas library for data manipulation and analysis
import pandas as pd
# Import numpy for numerical operations
import numpy as np

# Create a sample dataset with missing values and inconsistencies
data = {
    'Name': ['John', 'Jane', 'Bob', None, 'Alice', 'Charlie'],
    'Age': [25, 30, None, 35, 28, 22],
    'Salary': [50000, 60000, 55000, 65000, None, 52000],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance'],
    'Email': ['john@example.com', 'jane@example.com', 'bob@example.com', 'david@example.com', 'alice@example.com', 'CHARLIE@EXAMPLE.COM']
}

print("Data Cleaning and Preparation with Pandas\n")

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the original dataset
print("Original Dataset:")
print(df)
print("\n")

# Check the data types of each column
print("Data Types:")
print(df.dtypes)
print("\n")

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())
print("\n")

# Check for missing values in the dataset
print("Missing Values:")
print(df.isnull().sum())
print("\n")

# Drop rows with any missing values
df_dropped = df.dropna()
print("After dropping rows with missing values:")
print(df_dropped)
print("\n")

# Fill missing values with mean for Age column
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing values with median for Salary column
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# Fill missing values with forward fill method for Name column
#df['Name'] = df['Name'].fillna(method='ffill')

# finally fill any remaining missing with sentinel
df['Name'] = df['Name'].fillna('Unknown')

# Display dataset after filling missing values
print("After filling missing values:")
print(df)
print("\n")

# Remove duplicates if any
df = df.drop_duplicates()
print("After removing duplicates:")
print(df)
print("\n")

# Convert Email to lowercase for standardization
df['Email'] = df['Email'].str.lower()
print("After standardizing Email (lowercase):")
print(df)
print("\n")

# Strip whitespace from string columns
df['Name'] = df['Name'].str.strip()
print("After stripping whitespace:")
print(df)
print("\n")

# Remove outliers from Salary column using IQR method
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Salary'] >= Q1 - 1.5 * IQR) & (df['Salary'] <= Q3 + 1.5 * IQR)]
print("After removing outliers from Salary:")
print(df)
print("\n")

# Reset index after filtering
df = df.reset_index(drop=True)
print("After resetting index:")
print(df)
print("\n")

# Display descriptive statistics
print("Descriptive Statistics:")
print(df.describe())
print("\n")

# Display final cleaned dataset
print("Final Cleaned Dataset:")
print(df)

#Combine with another dataset (for demonstration, we will create a new dataset)
new_data = {
    'Name': ['David', 'Eve'],
    'Age': [40, 35],
    'Salary': [70000, 65000],
    'Department': ['IT', 'HR'],
    'Email': ['david@example.com', 'eve@example.com']
}
new_df = pd.DataFrame(new_data)
print("New Dataset:")
print(new_df)
print("\n")

# Concatenate the two datasets
combined_df = pd.concat([df, new_df], ignore_index=True)
print("Combined Dataset:")
print(combined_df)
print("\n")
# Merge with another dataset (for demonstration, we will create a new dataset with additional information)
additional_data = {
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'David', 'Eve'],
    'Experience': [5, 7, 3, 4, 2, 10, 8]
}
additional_df = pd.DataFrame(additional_data)
print("Additional Dataset:")
print(additional_df)
print("\n")

# Merge the datasets on the 'Name' column
merged_df = pd.merge(df, additional_df, on='Name', how='left')
print("Merged Dataset:")
print(merged_df)
print("\n") 

# Save the cleaned dataset to a new CSV file
merged_df.to_csv('cleaned_dataset.csv', index=False)    
print("Cleaned dataset saved to 'cleaned_dataset.csv'")
