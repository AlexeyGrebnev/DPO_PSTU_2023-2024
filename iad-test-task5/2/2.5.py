import numpy as np

data = np.loadtxt('scipy-lectures.txt')
year, hares, lynxes, carrots = data.T  # колонки в переменные

import matplotlib.pyplot as plt
plt.axes([0.2, 0.1, 0.5, 0.8]) 

plt.plot(year, hares, year, lynxes, year, carrots) 

plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5)) 

plt.show()

