########################################################################
# Armadillos, Cameron Blochwitz, Brendan Boyd, Trevor Franklin, Per Halvorsen
# AST 304, Fall 2018
# Michigan State University
########################################################################
import numpy as np
import matplotlib.pyplot as plt
from kepler import *
from ode import *

"""
This prgoram plots the calculated trajectories for each imported ode.
In order for it to run it must have both the ode.py and kepler.py
files in the same directory.

Simply running the code will give you two plots for each ODE; one for
the trajectory and one for the energies as a function of time.
"""

# use this to identify methods
integration_methods = {
    'Euler':fEuler,
    'RK2':rk2,
    'RK4':rk4
    }

#sets initial values
test = np.arange(0,1024)
h = np.zeros(11)
e = 0.5
a = 1
m = 1
eknown = -1/2.


#calculate the errors for each system we used
def simulation(a=a, m=m, e=e, method='fEuler'):
    """
    Simulates orbit for given method. Returns trajectories for
    smallest and largest h, as well as energies throughout
    orbit.

    Arguments
        a (scalar)
            semi-major axis
        m (scalar)
            mass normalized
        e (scalar)
            eccentricity
        method (function)
            ODE used for that simulation
    """
    z0, eps0, Tperiod = set_initial_conditions(a, m, e)
    h0 = 0.1*Tperiod
    for i in range(11):
        if(i==0):
            ts_low, Xs_low, Ys_low, KEs_low, PEs_low, TEs_low = integrate_orbit(z0, m, 3*Tperiod, h0, method)
        if(i==10):
            ts_hi, Xs_hi, Ys_hi, KEs_hi, PEs_hi, TEs_hi = integrate_orbit(z0, m, 3*Tperiod, h0, method)
        #ts, Xs, Ys, KEs, PEs, TEs = integrate_orbit(z0, m, 2*Tperiod, h0, method)
        h0 = h0/2

    energies_hi = [KEs_low, PEs_low, TEs_low]
    energies_low = [KEs_hi, PEs_hi, TEs_hi]

    return Xs_low, Ys_low, Xs_hi, Ys_hi, energies_low, energies_hi, ts_low, ts_hi


#Plots both trajectories and E(t)
for ode_type in integration_methods:
    x1,y1,x2,y2, energies_small_step, energies_large_step, t1, t2 = simulation(method=ode_type)
    plt.plot(x1, y1, 'b', label="Large stepsize")
    plt.plot(x2, y2, 'r', label="Small stepsize")
    plt.hlines(0, 0.5, 1.5, 'k', linestyle = '--', label="semi-major axis")
    #plt.annotate(s='', xy=(1.5, 0), xytext=(0.5,0), arrowprops=dict(arrowstyle='<->'))
    plt.title("Trajectories for {0}".format(ode_type))
    plt.xlabel("x (AU)")
    plt.ylabel("y (AU)")
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.legend()
    plt.show()

    #plot energies for small time steps
    K, P, TE = energies_large_step
    plt.plot(t1, K, label="Kinetic")
    plt.plot(t1, P, label="Potential")
    plt.plot(t1, TE, label="Total Energy")
    plt.title("Energies for {0} (large time steps)".format(ode_type))
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.legend()
    plt.show()

    #plot energies for large time step
    K, P, TE = energies_small_step
    plt.plot(t2, K, label="Kinetic")
    plt.plot(t2, P, label="Potential")
    plt.plot(t2, TE, label="Total Energy")
    plt.title("Energies for {0} (small time steps)".format(ode_type))
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.legend()
    plt.show()
