#Import libraries
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas
import numpy as np


"""
This file reads and plots data from a csv file
"""


# Quarter mintue intervals
trip_data = pandas.read_csv("trip_per_quarter_minute.csv")
qmin_interval = trip_data["qmin_interval"]
num_trips = trip_data["num_trips"]


# Convert to percentages
prob_trips = num_trips/sum(num_trips)

print(np.mean(num_trips))


# Finding values for log normal PDF
V = (sum((qmin_interval - np.mean(prob_trips))**2)/len(prob_trips))
mu = np.mean(prob_trips) #This values did not match needed parameters
s = np.sqrt(V) #This values did not match needed parameters
x = np.linspace(0, 300, 2000)
s = .75
loc = 1
e_mu = 40


# Plotting everything
plt.bar(qmin_interval, prob_trips, label='my data')
plt.plot(x, stats.lognorm.pdf(x, s, loc, e_mu), label='lognorm(x,{},{},{})'.format(s, loc, e_mu), color='salmon')
plt.legend()
plt.xlabel("1 interval = a quarter minute")
plt.ylabel("Probabilty of trip")
plt.xlim(left=0, right=300)
plt.ylim(bottom=0)
plt.title("Probabilty Distribution")
plt.show()


# Half minute intervals
trip_data = pandas.read_csv("trips_per_half_minute.csv")
half_min_interval = trip_data["half_min_interval"]
num_trips = trip_data["num_trips"]

prob_trips = num_trips/sum(num_trips)

# Finding values for log normal PDF
V = (sum((half_min_interval - np.mean(prob_trips))**2)/len(prob_trips))
mu = np.mean(prob_trips) #This values did not match needed parameters
s = np.sqrt(V) #This values did not match needed parameters
x = np.linspace(0, 150, 1000)
s = .75
loc = 1
e_mu = 20

# Plotting everything
plt.plot(half_min_interval, prob_trips, label='my data')
plt.plot(x, stats.lognorm.pdf(x, s, loc, e_mu), label='lognorm(x,{},{},{})'.format(s, loc, e_mu))
plt.legend()
plt.xlabel("1 interval = a half minute")
plt.ylabel("Probabilty of trip")
plt.xlim(left=0, right=150)
plt.ylim(bottom=0)
plt.title("Probabilty Distribution")
plt.show()
