import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [5, 7, 8, 6, 9]

plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(x, y1)
plt.title('Line Plot')

plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.bar(x, y2)
plt.title('Bar Plot')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()