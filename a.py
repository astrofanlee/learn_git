import numpy as np
import matplotlib.pyplot as plt

a = np.random.random(1000*1000)
plt.pcolormesh(a)
plt.figure(figsize=(12,9))
plt.savefig('graph_a.png')
