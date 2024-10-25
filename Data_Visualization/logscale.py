import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 100, 100)
y = np.log(x)

plt.plot(x, y)
plt.title('Logarithmic Scale Example')
plt.xlabel('X-axis')
plt.show()