import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

X_b = np.c_[np.ones((len(X), 1)), X]

theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

X_new = np.array([[0], [2], [3]])
X_new_b = np.c_[np.ones((len(X_new), 1)), X_new]
y_predict = X_new_b.dot(theta_best)

print("Predictions:", y_predict)