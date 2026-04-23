# Task 3: Customer Classification (High-value vs Low-value)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Generate synthetic customer data
np.random.seed(42)
num_samples = 300
data = pd.DataFrame({
	'total_spending': np.random.normal(1000, 400, num_samples).clip(100, 3000),
	'age': np.random.normal(35, 10, num_samples).clip(18, 70),
	'num_visits': np.random.poisson(10, num_samples),
	'purchase_freq': np.random.uniform(0.5, 5, num_samples)
})

# Assign high-value (1) if spending > 1200 and visits > 10, else low-value (0)
data['value'] = ((data['total_spending'] > 1200) & (data['num_visits'] > 10)).astype(int)

# 2. Data cleaning: introduce some missing values and outliers for demonstration
data.loc[np.random.choice(num_samples, 5), 'age'] = np.nan
data.loc[np.random.choice(num_samples, 3), 'total_spending'] = 5000  # outliers


# Handle missing values (fill with mean) - avoid chained assignment warning
data['age'] = data['age'].fillna(data['age'].mean())

# Double-check for any remaining NaNs in all features (drop rows with any NaN)
data = data.dropna(subset=['total_spending', 'age', 'num_visits', 'purchase_freq', 'value'])

# Handle outliers (cap spending at 3000)
data['total_spending'] = np.where(data['total_spending'] > 3000, 3000, data['total_spending'])

# 3. Feature scaling
features = ['total_spending', 'age', 'num_visits', 'purchase_freq']
scaler = StandardScaler()
data_scaled = data.copy()
data_scaled[features] = scaler.fit_transform(data[features])

# 4. Train-test split
X = data_scaled[features]
y = data_scaled['value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 5. Train classifier (Logistic Regression)
clf = LogisticRegression()
clf.fit(X_train, y_train)

# 6. Find separating hyperplane (coefficients)
print("Model coefficients (hyperplane):")
for feat, coef in zip(features, clf.coef_[0]):
	print(f"  {feat}: {coef:.3f}")
print(f"Intercept: {clf.intercept_[0]:.3f}")

# 7. Find rules (feature importance)
print("\nRules for classification (higher coef = more important):")
for feat, coef in sorted(zip(features, clf.coef_[0]), key=lambda x: abs(x[1]), reverse=True):
	print(f"  If {feat} increases, odds of being high-value {'increase' if coef > 0 else 'decrease'} (coef={coef:.2f})")

# 8. Evaluate model
y_pred = clf.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# 9. Visualize results
plt.figure(figsize=(6,4))
sns.countplot(x='value', data=data)
plt.title('High-value vs Low-value Customers (True Distribution)')
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
