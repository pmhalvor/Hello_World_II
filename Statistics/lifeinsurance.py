#Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
This file reads data from a file, and plots the cumulative and point probabilities

This is written specifically for the file dodelighet-felles.txt in this same folder
"""

#Read in data and exctract vectors of age and death rates of men
deatheveryone = pd.read_csv("dodelighet-felles.txt", sep="\t")
age   = deatheveryone["ald"].values
dead  = deatheveryone["dod"].values

#Yearly death probs
qx = dead/1000

#Calculate cumulative distribution for X remaining years alive
Fx = 1 - np.cumprod(1- qx[30:107])

#Plot cum dist.
remainder = np.arange(0, 77)
plt.step(remainder, Fx, where="post")
plt.xlabel("Remaining life")
plt.ylabel("Cumulative distribution")
plt.show()

#Calculate point probabilty
tmp = np.zeros(77)
tmp[1:77] = Fx[0:76]
px = Fx - tmp

#Plot point porb.
plt.bar(remainder, px, width=1, edgecolor="black")
plt.xlabel("Remaining lifetime")
plt.ylabel("Point probability")
plt.show()

#Calculate expected current valued coverage payments
indicies = np.arange(0, 35)
EhX = sum(1000000*px[0:35]/1.03**indicies)

# Calculate expected current valued premium per kr (K=1)
indicies2 = np.arange(1,36)
EgX = (1-sum((1/1.03)**indicies2*px[0:35])-(1/1.03)**35*sum(px[35:77]))/(1-1/1.03)

#Calculate
premium = EhX/EgX
print("Premium is {:10.4f},- kr to break even".format(premium))
