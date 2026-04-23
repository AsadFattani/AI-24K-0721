# Task 3: K-Means Clustering for Student Grouping
# References: see 1_EDA_STUDENT_PERFORMANCE_.ipynb for pandas, numpy, matplotlib, seaborn, and scaling examples

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv('LAB 12\py files\student_cluster_data.csv')

features = ['GPA', 'study_hours', 'attendance_rate']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertia = []
k_range = range(2, 7)
for k in k_range:
	kmeans = KMeans(n_clusters=k, random_state=42)
	kmeans.fit(X_scaled)
	inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(
	data=df,
	x='study_hours',
	y='GPA',
	hue='cluster',
	palette='Set1',
	s=80,
	edgecolor='k'
)
plt.title('Student Clusters by Study Hours and GPA')
plt.xlabel('Average Weekly Study Hours')
plt.ylabel('GPA')
plt.legend(title='Cluster')
plt.tight_layout()
plt.show()

print(df[['student_id', 'cluster']])
