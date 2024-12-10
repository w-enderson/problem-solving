import numpy as np
import matplotlib.pyplot as plt

x = np.array([i for i in range(1964, 1975)])
y = np.array([
                27.614, 44.073, 63.746, 86.171, 
                122.430, 161.900, 208.300, 276.807, 
                363.167, 498.307, 719.519
            ])

# 2) a) não é estacionária;
print(y)
plt.plot(x, y, marker='o', linestyle='-')
plt.grid()
plt.show()

# 2)b) primeira diferença não é estácionária;
delta_z1 = np.diff(y)
print(delta_z1)
plt.plot(x[1:], delta_z1, marker='o', linestyle='-')
plt.grid()
plt.show()

# 2)c) segunda diferença também não é estácionária;
delta_z2 = np.diff(delta_z1)
print(delta_z2)
plt.plot(x[2:], delta_z2, marker='o', linestyle='-')
plt.grid()
plt.show()







