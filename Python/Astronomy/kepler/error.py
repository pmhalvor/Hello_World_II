########################################################################
# Armadillos, Cameron Blochwitz, Brendan Boyd, Trevor Franklin, Per Halvorsen
# AST 304, Fall 2018
# Michigan State University
########################################################################

#This file is used to calcuate the error of our functions with a known result

import numpy as np
import matplotlib.pyplot as plt
from kepler import *
from ode import *

#Label methods
integration_methods = {
    'Euler':fEuler,
    'RK2':rk2,
    'RK4':rk4
    }

#Initial values for this specific problem
test = np.arange(0,1024)
h = np.zeros(11)
e = 0.5
a = 1
m = 1
eknown = -1/2.

#Calculate the errors for each system we used
def TE(a, m, e, method='fEuler'):
    z0, eps0, Tperiod = set_initial_conditions(a, m, e)
    h0 = 0.1*Tperiod
    total_energy_num = np.zeros(11)
    for i in range(11):
        h[i] = h0
        ts, Xs, Ys, KEs, PEs, TEs = integrate_orbit(z0, m, 3*Tperiod, h0, method)
        total_energy_num[i] = TEs[-1]
        h0 = h0/2
    return total_energy_num

#Creates array of the different errors for each method
errorfe = 1/(abs(eknown - TE(a, m, e, method='Euler'))/abs(eknown))
errorrk2 = 1/(abs(eknown - TE(a, m, e, method='RK2'))/abs(eknown))
errorrk4 = 1/(abs(eknown - TE(a, m, e, method='RK4'))/abs(eknown))

#plot all figures with errors, each should end up with a different color from the others
plt.plot(h, errorfe,  label="Error on Forward Euler")
plt.plot(h, errorrk2, label="Error on RK2")
plt.plot(h, errorrk4, label="Error on RK4")
plt.title("Error vs Timestep Size for 3 Systems")
plt.xlabel("Timestep (H0/Number)")
plt.ylabel("Error")
plt.legend()
plt.yscale('log')
plt.show()
