from sklearn.datasets import load_diabetes  # import diabetes dataset loader
import pandas as pd  # import pandas for data handling
import seaborn as sns  # import seaborn for visualization
import matplotlib.pyplot as plt  # import matplotlib for plotting
from sklearn.feature_selection import mutual_info_regression  # import mutual information function

# Load the dataset
data = load_diabetes()  # load diabetes data from sklearn
# Create a DataFrame from the data with feature names
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target  # add the target variable to the DataFrame

# Display Dataset information
print(df.head())  # print the first rows
print(df.info())  # print dataset info including dtypes and non-null counts

# Calculate correlation matrix
correlation_matrix = df.corr()  # compute correlation among features and target

# Plot heatmap
plt.figure(figsize=(10,8))  # create a figure with specified size
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")  # plot heatmap of correlations
plt.title("Correlation Matrix")  # set title for the heatmap
plt.show()  # display the plot

# Select features with high correlation to the target
correlated_features = correlation_matrix['target'].sort_values(ascending=False)  # sort target correlations
print("Features Most Correlated with Target:")  # print label for correlated features
print(correlated_features)  # print sorted correlations with target

# Seperate featured and target
X = df.drop(columns=['target'])  # separate input features from target
y = df['target']  # assign target variable

# Calculate mutual information
mutual_info = mutual_info_regression(X, y)  # compute mutual information between features and target

# Create a Dataframe for better visualization
mi_df = pd.DataFrame({'Feature': X.columns, "Mutual Information": mutual_info})  # build DataFrame of MI scores
mi_df = mi_df.sort_values(by="Mutual Information", ascending=False)  # sort features by MI score

print("Mutual Information Scores:")  # print label for mutual information results
print(mi_df)  # print mutual information DataFrame

from sklearn.ensemble import RandomForestRegressor  # import Random Forest regressor

# Train a Random Forest Model
model = RandomForestRegressor(random_state=42)  # initialize model with random state for reproducibility
model.fit(X, y)  # train model on the dataset

# Get feature importance
feature_importance = model.feature_importances_  # extract feature importance scores
importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importance})  # create DataFrame for importances
importance_df = importance_df.sort_values(by='Importance', ascending=False)  # sort importances descending

print("Feature Importance from Random Forest:")  # print label for importance results
print(importance_df)  # print feature importance DataFrame

# Plot feature importance
plt.figure(figsize=(10,6))  # create a figure for the importance plot
plt.barh(importance_df['Feature'], importance_df['Importance'])  # plot horizontal bar chart of importances
plt.gca().invert_yaxis()  # invert y-axis to show the most important feature at top
plt.title("Feature Importance from Random Forest")  # set title for the importance plot
plt.show()  # display the importance plot