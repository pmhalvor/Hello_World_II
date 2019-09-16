import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt


"""
This file will read a .csv of the names of stations per year,
and print out lists of the newly added stations per year.
"""

# Read in data
data = pd.read_csv("new_stations.csv")
names = data['names']
years = data['years']

# Lists that will hold all new stations
new_2014 = []
new_2015 = []
new_2016 = []

# Checking years with previous index
for i in range(len(names)):
	if int(years[i])!=2013:
		if names[i]!=names[i-1]:
			# Station is new
			if int(years[i])==2014:
				new_2014.append(names[i])
				f = open('new_2014.txt', 'a+')
				f.write(names[i]+',\n')
				f.close()
			elif int(years[i])==2015:
				new_2015.append(names[i])
				f = open('new_2015.txt', 'a+')
				f.write(names[i]+',\n')
				f.close()
			elif int(years[i])==2016:
				new_2016.append(names[i])
				f = open('new_2016.txt', 'a+')
				f.write(names[i]+',\n')
				f.close()

print(len(new_2014))
print(len(new_2015))
print(len(new_2016))


# Generate savable lists of new stations
# fig = go.Figure(data=[go.Table(header=dict(values=['2014', '2015', 2016]),
# 				cells=dict(values=[new_2014, new_2015, new_2016]))
# 					])
#
# fig.show()
#
# my_table = plt.table(cellText=new_2014,
# 						colLabels=(2014))
# plt.show()
