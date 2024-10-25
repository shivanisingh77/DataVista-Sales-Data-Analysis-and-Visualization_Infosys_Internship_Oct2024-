import numpy as np

# Calculate probabilities
def calculate_probabilities(X, y):
    unique_classes = np.unique(y)
    probabilities = {}
    
    for label in unique_classes:
        X_class = X[y == label]
        probabilities[label] = {}
        probabilities[label]['prior'] = len(X_class) / len(y)
        probabilities[label]['mean'] = np.mean(X_class, axis=0)
        probabilities[label]['var'] = np.var(X_class, axis=0)
    
    return probabilities

# Gaussian probability
def gaussian_probability(x, mean, var):
    coeff = 1 / np.sqrt(2 * np.pi * var)
    exponent = np.exp(-(x - mean)**2 / (2 * var))
    return coeff * exponent

# Predict class label
def predict(X_test, probabilities):
    predictions = []
    for x in X_test:
        posteriors = {}
        for label, params in probabilities.items():
            prior = np.log(params['prior'])
            likelihood = np.sum(np.log(gaussian_probability(x, params['mean'], params['var'])))
            posteriors[label] = prior + likelihood
        predictions.append(max(posteriors, key=posteriors.get))
    return predictions

# Sample data
X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y_train = np.array([0, 0, 1, 1, 1])
X_test = np.array([[2.5, 3.5], [3.5, 4.5]])

# Run Naive Bayes classifier
probabilities = calculate_probabilities(X_train, y_train)
y_pred = predict(X_test, probabilities)
print("Predictions:", y_pred)