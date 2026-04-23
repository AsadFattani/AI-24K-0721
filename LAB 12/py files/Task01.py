
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"LAB 12\py files\student-por.csv",delimiter=';')

features = df.drop(['G3'], axis=1)

features_encoded = pd.get_dummies(features, drop_first=True)

kmeans_no_scaling = KMeans(n_clusters=2, random_state=42)
clusters_no_scaling = kmeans_no_scaling.fit_predict(features_encoded)
features_encoded['Cluster_No_Scaling'] = clusters_no_scaling

cols_to_scale = [col for col in features_encoded.columns if col != 'age' and not col.startswith('Cluster')]
scaler = StandardScaler()
features_scaled = features_encoded.copy()
features_scaled[cols_to_scale] = scaler.fit_transform(features_scaled[cols_to_scale])

kmeans_scaled = KMeans(n_clusters=2, random_state=42)
clusters_scaled = kmeans_scaled.fit_predict(features_scaled.drop('Cluster_No_Scaling', axis=1))
features_scaled['Cluster_Scaled'] = clusters_scaled

comparison = pd.DataFrame({
	'No_Scaling': features_encoded['Cluster_No_Scaling'],
	'With_Scaling': features_scaled['Cluster_Scaled']
})

print('Cluster assignment counts (No Scaling):')
print(features_encoded['Cluster_No_Scaling'].value_counts())
print('\nCluster assignment counts (With Scaling):')
print(features_scaled['Cluster_Scaled'].value_counts())

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
reduced_no_scaling = pca.fit_transform(features_encoded.drop('Cluster_No_Scaling', axis=1))
reduced_scaled = pca.fit_transform(features_scaled.drop(['Cluster_No_Scaling', 'Cluster_Scaled'], axis=1))

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.scatter(reduced_no_scaling[:,0], reduced_no_scaling[:,1], c=features_encoded['Cluster_No_Scaling'], cmap='viridis', alpha=0.6)
plt.title('Clusters without Scaling')
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.subplot(1,2,2)
plt.scatter(reduced_scaled[:,0], reduced_scaled[:,1], c=features_scaled['Cluster_Scaled'], cmap='viridis', alpha=0.6)
plt.title('Clusters with Scaling (except Age)')
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.tight_layout()
plt.show()

print("\nINSIGHTS:")
print("- Without scaling, features with larger numeric ranges dominate the clustering, possibly leading to biased clusters.")
print("- With scaling (except age), all features contribute more equally, potentially revealing different groupings.")
print("- Compare the cluster sizes and visual separation to see the effect of scaling.")
