#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd  # load pandas for data manipulation
from sklearn.model_selection import train_test_split  # import function to split data into train and test sets
import seaborn as sns  # import seaborn for plotting
import matplotlib.pyplot as plt  # import matplotlib for showing plots

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"  # dataset URL for tips data
df = pd.read_csv(url)  # read CSV data from URL into DataFrame
# Print information about the dataset
print("Data Info :\n",df.info())
# Print statistical summary of the dataset
print("Data Describe :\n",df.describe())

# Define features and target
# Select 'total_bill' and 'size' columns as features
features = df[['total_bill', 'size']]
# Select 'tip' column as target variable
target = df['tip']

# Display first 5 rows of features
print("Features: \n", features.head())
# Display first 5 rows of target
print("Target: \n", target.head())

# Split data into training and testing sets with 80-20 split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
# Print shape of training dataset
print("Training Data Set: ", X_train.shape)
# Print shape of testing dataset
print("Testing Data Set: ", X_test.shape)
# Create pairplot to visualize relationships between features and target
sns.pairplot(df, x_vars=["total_bill", "size"], y_vars="tip", height=5, aspect=0.8, kind="scatter")
# Add title to the plot
plt.title("Feature vs Target Relationships")
# Display the plot
plt.show()