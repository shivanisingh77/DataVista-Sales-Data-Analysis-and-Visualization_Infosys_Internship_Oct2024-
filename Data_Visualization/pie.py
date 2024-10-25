import matplotlib.pyplot as plt

sizes = [25, 35, 20, 20]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title('Simple Pie Chart')

plt.show()