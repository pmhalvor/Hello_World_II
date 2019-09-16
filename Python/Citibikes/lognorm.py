import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt



# Plot the theoretical density of f
s = 1 #The values that fit my data didnt match the math. Idk why...

mu = 0.005

x = np.linspace(0, 150, 1000)
plt.plot(x, stats.lognorm.pdf(x, 1, 0, 20), color='r')
plt.show()
