# Task 01: House Price Prediction
# Author: Data Scientist
# Description: Predict house prices using regression (scikit-learn)


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)  # Ensure reproducibility



# 1. Create a simple synthetic dataset (like sklearn examples)
num_samples = 100
df = pd.DataFrame({
    'square_footage': np.random.randint(1000, 3000, num_samples),
    'bedrooms': np.random.randint(2, 6, num_samples),
    'bathrooms': np.random.randint(1, 4, num_samples),
    'age': np.random.randint(0, 30, num_samples),
    'neighborhood': np.random.choice(['A', 'B', 'C'], num_samples)
})
# Simple price formula: sqft*150 + bedrooms*10000 + bathrooms*5000 - age*1000 + neighborhood effect + noise
neigh_map = {'A': 20000, 'B': 10000, 'C': 0}
df['price'] = (
    df['square_footage'] * 150
    + df['bedrooms'] * 10000
    + df['bathrooms'] * 5000
    - df['age'] * 1000
    + df['neighborhood'].map(neigh_map)
    + np.random.normal(0, 10000, num_samples)
)


# 2. Data Cleaning (simulate some missing values for demonstration)
for col in ['square_footage', 'bedrooms', 'bathrooms', 'age']:
    df.loc[df.sample(frac=0.05, random_state=42).index, col] = np.nan
df.loc[df.sample(frac=0.05, random_state=1).index, 'neighborhood'] = np.nan

# Show missing values
print("Missing values per column:\n", df.isnull().sum())

# Fill missing numeric values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)


# Fill missing categorical values with mode (fix chained assignment warning)
for col in df.select_dtypes(include=['object', 'str']).columns:
    mode_val = df[col].mode()[0]
    df.fillna({col: mode_val}, inplace=True)



# 3. Encode categorical variables (e.g., neighborhood)
le = LabelEncoder()
df['neighborhood'] = le.fit_transform(df['neighborhood'])


# 4. Feature Selection (correlation heatmap)
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# Assume 'price' is the target variable
X = df.drop('price', axis=1)
y = df['price']


# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Evaluation
predictions = model.predict(X_test)
print('Mean Squared Error:', mean_squared_error(y_test, predictions))
print('R^2 Score:', r2_score(y_test, predictions))



# 8. Predict price for a new house
# Example: 2000 sqft, 3 bedrooms, 2 bathrooms, 10 years old, neighborhood='B'
neigh_num = le.transform(['B'])[0]
new_house_df = pd.DataFrame({
    'square_footage': [2000],
    'bedrooms': [3],
    'bathrooms': [2],
    'age': [10],
    'neighborhood': [neigh_num]
})
predicted_price = model.predict(new_house_df)
print('Predicted price for new house:', predicted_price[0])
