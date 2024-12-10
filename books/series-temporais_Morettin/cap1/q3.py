import numpy as np
import matplotlib.pyplot as plt

x = np.array([i for i in range(1, 25)])
y = np.array([71.6, 72.5, 73.5, 74.5, 75.2, 76.3, 76.9, 78.1, 80.0, 80.9, 81.7, 82.9, 
              84.7, 86.3, 88.8, 90.9, 91.5, 93.4, 94.6, 95.9, 96.7, 97.8, 99.1, 100])

# 3) a) não é estacionária
plt.plot(x, y)
plt.show()

# 3) b) aproximadamente estacionária
for i in range(1, 4):
    y = np.diff(y)
    plt.plot(x[i:], y)
    plt.show()

