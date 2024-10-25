import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def gradient_descent(X, y, learning_rate, iterations):
    m = len(y)
    X_b = np.c_[np.ones((m, 1)), X]
    theta = np.random.randn(X_b.shape[1], 1)

    for i in range(iterations):
        z = X_b.dot(theta)
        predictions = sigmoid(z)
        gradients = X_b.T.dot(predictions - y) / m
        theta -= learning_rate * gradients

    return theta

X = np.array([[1], [2], [3], [4]])
y = np.array([[0], [0], [1], [1]])

theta_best = gradient_descent(X, y, learning_rate=0.1, iterations=1000)
print("Best parameters:", theta_best)

X_new = np.array([[1], [3]])
X_new_b = np.c_[np.ones((len(X_new), 1)), X_new]
predictions = sigmoid(X_new_b.dot(theta_best))
print("Predictions:", predictions)