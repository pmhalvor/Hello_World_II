import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

"""
This file gives an example of a Binominal distribution

Arguments:
    n = sample set

    p = probabilty in set
"""


# Set initial values
n = 25
p = 0.05

# create arrays
x   = np.arange(0, n)
pdf = binom.pmf(x, n, p)

# Plot prob. dist. func. as bar graph
plt.bar(x, pdf)
plt.xlabel("Number in sample size {:2d}".format(n))
plt.ylabel("Probability")
plt.title("Binomial Distribution sample size {:2d}".format(n))
plt.show()

# Find probability of different possible X (amount defect)
print(pdf)
print("P(X<=2)={:10.7f}".format(sum(pdf[0:3])))
print("P(X>=5)={:10.7f}".format(1-sum(pdf[0:5])))
print("P(X>=5)={:10.7f}".format(sum(pdf[5:])))
print("P(1<=X<=4)={:10.7f}".format(sum(pdf[1:5])))
print(pdf[0])

# Find expectation value
Ex = sum(x*pdf)
print("Expectation value {:7.5f}".format(Ex))

# Find variance and standard deviation
Ex2 = sum(pdf*(x**2))
Vx = Ex2 - Ex**2
print("Variance {:7.5f}".format(Vx))
print("Standard deviation {:7.5f}".format(np.sqrt(Vx)))
