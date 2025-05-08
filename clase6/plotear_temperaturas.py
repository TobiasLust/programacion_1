import matplotlib
import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.load('../Data/temperaturas.npy')
plt.hist(temperaturas,bins=30)
plt.show()





        