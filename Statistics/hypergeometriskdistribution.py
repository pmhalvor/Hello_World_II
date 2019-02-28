import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from scipy.special import binom as sbinom
"""
This file gives an example of a hypergeometric distribution

Arguements:
    x = amount of successful in sapmled set

    n = amount in sample set

    M = successful in total set

    N = amount in total set

"""
# Set initial values
X = 5
n = 6
M = 7
N = 12

# Create array of X's
x = np.arange(0, n+1)

# Find all binomial coefficients
success = sbinom(M,x)
nonsucc = sbinom(N-M,n-x)
allposs = sbinom(N,n)
h = success*nonsucc/allposs
print(h[X])

# Plot bar graph of distribution
plt.bar(x, success*nonsucc/allposs)
plt.show()

# Find specific instances of P(X=x)
