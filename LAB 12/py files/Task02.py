import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

data = {
	'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
	'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
	'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
	'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
	'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

df_encoded = df.copy()
df_encoded['vehicle_type_encoded'] = df_encoded['vehicle_type'].map({'SUV': 0, 'Sedan': 1, 'Truck': 2, 'Hatchback': 3})

features = ['mileage', 'fuel_efficiency', 'maintenance_cost', 'vehicle_type_encoded']
X = df_encoded[features]

kmeans_no_scaling = KMeans(n_clusters=3, random_state=42)
df['Cluster_No_Scaling'] = kmeans_no_scaling.fit_predict(X)
print("\nKMeans Clustering (No Scaling):")
print(df[['vehicle_serial_no', 'vehicle_type', 'Cluster_No_Scaling']])

scaler = StandardScaler()
X_scaled = X.copy()
X_scaled[['mileage', 'fuel_efficiency', 'maintenance_cost']] = scaler.fit_transform(X_scaled[['mileage', 'fuel_efficiency', 'maintenance_cost']])

kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['Cluster_Scaled'] = kmeans_scaled.fit_predict(X_scaled)
print("\nKMeans Clustering (With Scaling):")
print(df[['vehicle_serial_no', 'vehicle_type', 'Cluster_Scaled']])

print("\nComparison of Clustering Results:")
print(df[['vehicle_serial_no', 'vehicle_type', 'Cluster_No_Scaling', 'Cluster_Scaled']])

print("\nAnalysis:")
print("- Without scaling, features with larger numeric ranges (like mileage) dominate the clustering.")
print("- With scaling, all features contribute more equally, leading to different cluster assignments.")
