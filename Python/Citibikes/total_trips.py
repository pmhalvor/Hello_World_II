#Import libraries
import matplotlib.pyplot as plt
import pandas
import numpy as np

# This file is to count the total number of trips 
trip_data = pandas.read_csv("total_dataset.csv")
half_min_interval = trip_data["hmin_interval"]
num_trips = trip_data["num_trips"]

print(sum(num_trips))
