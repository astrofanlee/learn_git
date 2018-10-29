import numpy as np
import matplotlib.pyplot as plt

a = np.random.random(1000*1000)
plt.pcolormesh(a)
plt.savefig('graph_a.png')
