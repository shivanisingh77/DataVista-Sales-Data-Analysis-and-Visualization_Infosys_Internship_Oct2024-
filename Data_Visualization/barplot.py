import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, color='blue')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Plot')

plt.show()