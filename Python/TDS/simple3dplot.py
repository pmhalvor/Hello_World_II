from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

#Make data
X = [0,1,2,3,4,5,6,7,8,9]
Y = [0,1,2,3,4,5,6,7,8,9]
X, Y = np.meshgrid(X,Y)
Z = np.sqrt(X**2 + Y**2)

#Plot surface
surf = ax.plot_surface(X,Y,Z, cmap=cm.coolwarm)

#Add colorbar
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
