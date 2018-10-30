import numpy as np
import matplotlib.pyplot as plt

a = np.random.random((1000, 1000))
b = a ** 2
plt.figure(figsize=(12,9))
plt.pcolormesh(a)
plt.xlabel('x label')
plt.ylabel('y label')
plt.grid()
plt.savefig('graph_a.png')
plt.show()

