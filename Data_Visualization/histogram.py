import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(data, bins=5, color='green')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Simple Histogram')

plt.show()