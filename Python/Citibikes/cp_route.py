import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
This file breaks down the durations spent on the most popular route
"""

# Read in data
data = pd.read_csv("cp_route_times.csv")
time = data['cp_route_times']
num_trips = data['num_trips']

# Plot data
plt.axvline(x=30, color='r')
plt.axvline(x=60, color='r')
plt.axvline(x=90, color='r')
plt.axvline(x=120, color='r')
plt.axvline(x=150, color='r')
plt.bar(time[:180], num_trips[:180])
plt.xlim(left=0, right=180)
plt.xlabel("Minutes Spent on bike")
plt.ylabel("Amount of riders")
plt.show()
