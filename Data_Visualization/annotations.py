import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.title('Plot with Annotations')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')


plt.annotate('Peak Point', xy=(5, 11), xytext=(3, 10),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()