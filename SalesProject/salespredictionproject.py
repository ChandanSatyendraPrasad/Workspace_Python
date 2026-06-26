# =============================================================================
# READING AND EXPLORING THE ONLINE SALES DATASET
# Dataset: https://raw.githubusercontent.com/KC2016/sales_2025/refs/heads/main/data/online_sales_data.csv
# =============================================================================

# -----------------------------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES
# -----------------------------------------------------------------------------

# Import pandas for data manipulation and analysis
import pandas as pd

# Import numpy for numerical operations
import numpy as np

# Import matplotlib for basic plotting
import matplotlib.pyplot as plt

# Import seaborn for advanced statistical visualization
import seaborn as sns

# Import warnings to suppress unnecessary warnings
import warnings

# Set warnings to ignore mode
warnings.filterwarnings('ignore')

# Set display option to show all columns
pd.set_option('display.max_columns', None)

# -----------------------------------------------------------------------------
# STEP 2: READ THE DATASET FROM URL
# -----------------------------------------------------------------------------

# Define the URL of the dataset
url = "https://raw.githubusercontent.com/KC2016/sales_2025/refs/heads/main/data/online_sales_data.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(url)

# Print confirmation message
print("✅ Dataset loaded successfully!")
print("-" * 70)

# -----------------------------------------------------------------------------
# STEP 3: DISPLAY FIRST AND LAST FEW ROWS
# -----------------------------------------------------------------------------

# Display the first 10 rows to see the structure
print("\n📌 FIRST 10 ROWS:")
print(df.head(10))

# Display the last 5 rows to check data consistency
print("\n📌 LAST 5 ROWS:")
print(df.tail())

# -----------------------------------------------------------------------------
# STEP 4: CHECK DATASET SHAPE
# -----------------------------------------------------------------------------

# Print number of rows and columns
print("\n📌 DATASET SHAPE:")
print(f"  Total Rows:    {df.shape[0]}")
print(f"  Total Columns: {df.shape[1]}")

# -----------------------------------------------------------------------------
# STEP 5: DISPLAY COLUMN NAMES
# -----------------------------------------------------------------------------

# Print all column names with index
print("\n📌 COLUMN NAMES:")
for idx, col in enumerate(df.columns, 1):
    print(f"  {idx}. {col}")

# -----------------------------------------------------------------------------
# STEP 6: CHECK DATA TYPES OF EACH COLUMN
# -----------------------------------------------------------------------------

# Display data type information for all columns
print("\n📌 DATA TYPES:")
print(df.dtypes)

# -----------------------------------------------------------------------------
# STEP 7: DETAILED DATASET INFO
# -----------------------------------------------------------------------------

# Display comprehensive info including memory usage
print("\n📌 DETAILED INFO:")
df.info()

# -----------------------------------------------------------------------------
# STEP 8: CHECK FOR MISSING VALUES
# -----------------------------------------------------------------------------

# Count missing values in each column
print("\n📌 MISSING VALUES COUNT:")
print(df.isnull().sum())

# Calculate and display missing values percentage
print("\n📌 MISSING VALUES PERCENTAGE:")
missing_pct = (df.isnull().sum() / len(df)) * 100
print(missing_pct.round(2))

# Total missing values in entire dataset
total_missing = df.isnull().sum().sum()
print(f"\n  Total Missing Values in Dataset: {total_missing}")

# -----------------------------------------------------------------------------
# STEP 9: CHECK FOR DUPLICATE ROWS
# -----------------------------------------------------------------------------

# Count duplicate rows
duplicate_count = df.duplicated().sum()

print("\n📌 DUPLICATE ROWS:")
print(f"  Number of Duplicate Rows: {duplicate_count}")

# If duplicates exist, show them
if duplicate_count > 0:
    print("\n  Duplicate Rows:")
    print(df[df.duplicated(keep=False)])

# -----------------------------------------------------------------------------
# STEP 10: STATISTICAL SUMMARY FOR NUMERICAL COLUMNS
# -----------------------------------------------------------------------------

# Display summary statistics for numerical columns
print("\n📌 STATISTICAL SUMMARY (NUMERICAL COLUMNS):")
print(df.describe().round(2))

# -----------------------------------------------------------------------------
# STEP 11: STATISTICAL SUMMARY FOR CATEGORICAL COLUMNS
# -----------------------------------------------------------------------------

# Display summary for categorical/object columns
print("\n📌 STATISTICAL SUMMARY (CATEGORICAL COLUMNS):")
print(df.describe(include=['object', 'category']))

# -----------------------------------------------------------------------------
# STEP 12: UNIQUE VALUES IN EACH COLUMN
# -----------------------------------------------------------------------------

# Count unique values for each column
print("\n📌 UNIQUE VALUES COUNT:")
for col in df.columns:
    unique_count = df[col].nunique()
    print(f"  {col}: {unique_count} unique values")

# -----------------------------------------------------------------------------
# STEP 13: DISPLAY UNIQUE VALUES FOR CATEGORICAL COLUMNS
# -----------------------------------------------------------------------------

# Identify categorical columns (object or category dtype)
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

print("\n📌 UNIQUE VALUES IN CATEGORICAL COLUMNS:")
for col in categorical_cols:
    unique_vals = df[col].unique()
    print(f"\n  {col} ({len(unique_vals)} unique):")
    # Show all unique values if less than 20, otherwise show first 20
    if len(unique_vals) <= 20:
        for val in unique_vals:
            # Count occurrences of each unique value
            count = df[col].value_counts().get(val, 0)
            print(f"    - {val} ({count} times)")
    else:
        for val in unique_vals[:20]:
            count = df[col].value_counts().get(val, 0)
            print(f"    - {val} ({count} times)")
        print(f"    ... and {len(unique_vals) - 20} more")

# -----------------------------------------------------------------------------
# STEP 14: SEPARATE NUMERICAL AND CATEGORICAL COLUMNS
# -----------------------------------------------------------------------------

# Get list of numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Get list of categorical columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

print("\n📌 COLUMN CLASSIFICATION:")
print(f"\n  Numerical Columns ({len(numerical_cols)}):")
for col in numerical_cols:
    print(f"    - {col}")

print(f"\n  Categorical Columns ({len(categorical_cols)}):")
for col in categorical_cols:
    print(f"    - {col}")

# -----------------------------------------------------------------------------
# STEP 15: CHECK FOR OUTLIERS IN NUMERICAL COLUMNS USING IQR METHOD
# -----------------------------------------------------------------------------

print("\n📌 OUTLIER DETECTION (IQR Method):")

# Loop through each numerical column
for col in numerical_cols:
    # Calculate Q1 (25th percentile)
    Q1 = df[col].quantile(0.25)
    
    # Calculate Q3 (75th percentile)
    Q3 = df[col].quantile(0.75)
    
    # Calculate Interquartile Range (IQR)
    IQR = Q3 - Q1
    
    # Define lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Count outliers below lower bound
    outliers_below = df[df[col] < lower_bound].shape[0]
    
    # Count outliers above upper bound
    outliers_above = df[df[col] > upper_bound].shape[0]
    
    # Total outliers in this column
    total_outliers = outliers_below + outliers_above
    
    # Print outlier information
    print(f"\n  {col}:")
    print(f"    Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"    Lower Bound: {lower_bound:.2f}, Upper Bound: {upper_bound:.2f}")
    print(f"    Outliers Below: {outliers_below}, Outliers Above: {outliers_above}")
    print(f"    Total Outliers: {total_outliers}")

# -----------------------------------------------------------------------------
# STEP 16: CORRELATION MATRIX FOR NUMERICAL COLUMNS
# -----------------------------------------------------------------------------

print("\n📌 CORRELATION MATRIX:")
# Calculate correlation only for numerical columns
correlation = df[numerical_cols].corr()
print(correlation.round(3))

# -----------------------------------------------------------------------------
# STEP 17: VALUE COUNTS FOR KEY CATEGORICAL COLUMNS
# -----------------------------------------------------------------------------

print("\n📌 VALUE COUNTS FOR CATEGORICAL COLUMNS:")
for col in categorical_cols:
    print(f"\n  {col}:")
    print(df[col].value_counts().to_string())

# -----------------------------------------------------------------------------
# STEP 18: MEMORY USAGE INFORMATION
# -----------------------------------------------------------------------------

print("\n📌 MEMORY USAGE:")
print(df.memory_usage(deep=True))

# Total memory usage
total_memory = df.memory_usage(deep=True).sum()
print(f"\n  Total Memory Usage: {total_memory / 1024:.2f} KB")

# -----------------------------------------------------------------------------
# STEP 19: SAMPLE ROWS WITH ALL DETAILS
# -----------------------------------------------------------------------------

print("\n📌 SAMPLE 3 RANDOM ROWS:")
# Display 3 random rows for quick overview
print(df.sample(3, random_state=42))

# -----------------------------------------------------------------------------
# STEP 20: FINAL DATASET SUMMARY
# -----------------------------------------------------------------------------

print("\n" + "=" * 70)
print("📋 FINAL DATASET SUMMARY")
print("=" * 70)

print(f"\n  Dataset Name: Online Sales Data")
print(f"  Total Rows: {df.shape[0]}")
print(f"  Total Columns: {df.shape[1]}")
print(f"  Numerical Columns: {len(numerical_cols)}")
print(f"  Categorical Columns: {len(categorical_cols)}")
print(f"  Total Missing Values: {total_missing}")
print(f"  Total Duplicate Rows: {duplicate_count}")
print(f"  Memory Usage: {total_memory / 1024:.2f} KB")

print("\n" + "=" * 70)
print("✅ DATASET READING AND EXPLORATION COMPLETED!")
print("=" * 70)