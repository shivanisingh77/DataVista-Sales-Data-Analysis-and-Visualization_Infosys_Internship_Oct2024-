import numpy as np

# Sample data (each row is a data point)
X = np.array([[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0]])

# Standardize data (zero mean and unit variance)
X_meaned = X - np.mean(X, axis=0)

# Covariance matrix
cov_matrix = np.cov(X_meaned.T)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort eigenvectors by eigenvalues in decreasing order
idx = eigenvalues.argsort()[::-1]
eigenvectors = eigenvectors[:, idx]

# Transform the data to the new basis
X_pca = X_meaned.dot(eigenvectors)

print("PCA transformed data:\n", X_pca)