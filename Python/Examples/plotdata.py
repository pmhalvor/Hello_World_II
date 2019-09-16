import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('data.txt')

x = 'n'
y = 'time'

# Just change the column names
plt.xlabel(x)
plt.ylabel(y)
plt.plot(data[x], data[y])
plt.show()
