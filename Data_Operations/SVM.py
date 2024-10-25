import numpy as np

# Hinge loss function for SVM
def hinge_loss(X, y, w, b, reg_strength):
    n_samples = X.shape[0]
    distances = 1 - y * (np.dot(X, w) + b)
    losses = np.maximum(0, distances)
    return reg_strength * (np.sum(losses) / n_samples)

# Gradient descent for SVM
def gradient_descent(X, y, w, b, learning_rate, iterations, reg_strength):
    for _ in range(iterations):
        for i, x_i in enumerate(X):
            condition = y[i] * (np.dot(X[i], w) + b) >= 1
            if condition:
                w -= learning_rate * (2 * reg_strength * w)
            else:
                w -= learning_rate * (2 * reg_strength * w - np.dot(X[i], y[i]))
                b -= learning_rate * y[i]
    return w, b

# Sample data
X = np.array([[1, 2], [2, 3], [3, 3], [4, 5], [5, 6]])
y = np.array([1, 1, -1, -1, -1])

# Parameters
w = np.zeros(X.shape[1])
b = 0
learning_rate = 0.001
iterations = 1000
reg_strength = 0.01

# Train SVM
w, b = gradient_descent(X, y, w, b, learning_rate, iterations, reg_strength)
print("Weight vector:", w)
print("Bias term:", b)