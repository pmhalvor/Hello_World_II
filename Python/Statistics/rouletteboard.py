import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, nbinom

"""
This file gives an example of both a Binominal and Negative Binomial distributions

using an example of a roulette board.


Arguments:
    n = sample set

    k = fields played

    u = total number of fields on board

    p = probabilty in set

    m = cost per round

"""


# Set initial values
n = 24
k = 18.
u = 37
p = k/u
m = 25


# create arrays
x   = np.arange(0, n+1)  #VERY IMPORTANT TO HAVE n+1 HERE
pdf = binom.pmf(x, n, p)

# Plot prob. dist. func. as bar graph
plt.bar(x, pdf)
plt.xlabel("Number of wins out of {:2d}".format(n))
plt.ylabel("Probability")
plt.title("Binomial Distribution n={:2d} k={}".format(n, k))


# Part a)
print("\n a)")

# Find expectation value
Ex = sum(x*pdf)
print("Expectation value {:7.5f}".format(Ex))
print("Expectation value {:7.5f} (shortcut)".format(n*p))

# Find variance and standard deviation
Ex2 = sum(pdf*(x**2))
Vx = Ex2 - Ex**2
print("Variance {:7.5f}".format(Vx))
print("Variance {:7.5f} (shortcut)".format(n*p*(1-p)))
print("Standard deviation {:7.5f}".format(np.sqrt(Vx)))
print("Standard deviation {:7.5f}  (shortcut)".format(np.sqrt(n*p*(1-p))))


# Part b)
print("\n b)")

# Calculate expected nett gain
y = 25.*(36./k)*x - 25*n
Ey = sum(pdf*y)
Eys = m*(36./k)*Ex - m*n

# I found That you could also just multiply directly to the Ex we found earlier, but this process is difficult to implement on the next step
# win = 25*(36./k - 1)
# lose = -25.
# Ey = Ex*win + (n - Ex)*lose

print("Expected nett winnings {:7.5f}".format(Ey))
print("Expected nett winnings {:7.5f} (shortcut)".format(Eys))

# Calculate standard deviation of nett gain
Ey2 = sum(pdf*(y**2))
Vy = Ey2 - (Ey)**2
Vys = ((u-k)*n/k)*(m*(u-1)/u)**2

print("Standard deviation of winnings {:7.5f}". format(np.sqrt(Vy)))
print("Standard deviation of winnings {:7.5f} (shortcut)". format(np.sqrt(Vys)))


# Part c)
print("\n c)")

# At least 300,- kr in nett gains
i = 18      #She needs to win at least 18 times
print("Y = {} at index {}, which means she\'ll need to win at least {} rounds to go home with 300,-kr or more".format(y[i], i, i))

# At most -300,-kr in nett gains
j = 6
print("Y = {} at index {}, which means she\'ll need to win at least {} rounds to go home with -300,-kr or less".format(y[j], j, j))

print("P(Y>=300) = {}".format(sum(pdf[i:])))
print("P(Y<=-300) = {}".format(sum(pdf[:j])))


# Part d)
print("\n d)")

# Reset initial variables
k = 6.
p = k/u
pdf = binom.pmf(x, n, p)
y = 25.*(36./k)*x - 25*n

# Plot prob. dist. func. as bar graph
plt.bar(x, pdf)
plt.xlabel("Number of wins out of {:2d}".format(n))
plt.ylabel("Probability")
plt.title("Binomial Distribution n={:2d} k={}".format(n, k))

# At least 300,- kr in nett gains
i = 6     #He needs to win at least 6 times
print("Y = {} at index {}, which means she\'ll need to win at least {} rounds to go home with 300,-kr or more".format(y[i], i, i))

# At most -300,-kr in nett gains
j = 2
print("Y = {} at index {}, which means she\'ll need to win at least {} rounds to go home with -300,-kr or less".format(y[j], j, j))

print("P(Y>=300) = {}".format(sum(pdf[i:])))
print("P(Y<=-300) = {}".format(sum(pdf[:j])))


# Part e)
# print("\n e)")

# Reset initial variables
r = 3
k = 4.
p = k/u
n = 200     #Here n is arbitrarily chosen for the max amount of times she plays for computing purposes
z = np.arange(0, n)
y = 25.*(36./k)*z - 25*n
pdf = nbinom.pmf(z, r, p)
# print(y[:50])

# Plot prob. dist. func. as bar graph
plt.bar(z, pdf)
plt.xlabel("Number of losses before {} wins".format(r))
plt.ylabel("P(Z=z)=nb(z;{},{:5.2f})".format(r,p))
plt.title("Negative Binomial Distribution r={:2d} k={}".format(r, k))


# Part f)
print("\n f)")
# Nett gain of 300,- or more
i = 24
print("Y =  {} at index {}, which means she\'ll need to win at least {} rounds to go home with 300,-kr or more".format(y[i], i, i))

# Neet gain of -300,- or less
j = 20
print("Y = {} at index {}, which means she\'ll need to win at least {} rounds to go home with -300,- kr or less".format(y[j], j, j))

print("P(Y>=300) = {}".format(sum(pdf[:i])))
print("P(Y<=-300) = {}".format(sum(pdf[:j])))
