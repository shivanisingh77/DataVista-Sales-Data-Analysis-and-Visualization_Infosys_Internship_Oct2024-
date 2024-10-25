import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 8, 9, 12]

plt.scatter(x, y, color='red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')

plt.show()