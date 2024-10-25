import numpy as np
from collections import Counter

# Distance function
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b)**2))

# K-NN classifier
def knn(X_train, y_train, X_test, k=3):
    y_pred = []
    for test_point in X_test:
        distances = [euclidean_distance(test_point, x) for x in X_train]
        k_indices = np.argsort(distances)[:k]
        k_nearest_labels = [y_train[i] for i in k_indices]
        majority_vote = Counter(k_nearest_labels).most_common(1)[0][0]
        y_pred.append(majority_vote)
    return y_pred

# Sample data
X_train = np.array([[1, 1], [2, 2], [3, 3], [6, 6], [7, 7]])
y_train = np.array([0, 0, 0, 1, 1])
X_test = np.array([[4, 4], [5, 5]])

# Run K-NN classifier
y_pred = knn(X_train, y_train, X_test, k=3)
print("Predicted labels:", y_pred)