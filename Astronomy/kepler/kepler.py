########################################################################
# Armadillos, Cameron Blochwitz, Brendan Boyd, Trevor Franklin, Per Halvorsen
# AST 304, Fall 2018
# Michigan State University
########################################################################

"""
<Description of this module goes here: what it does, how it's used.>

This module contains routines for calculating the kinetic, potential,
total energies and derivatives of r and v with respect to time at a
given step. Routine 'integrate_orbit' uses one of the imported ODE's
to integrate over entire time interval 0<=t<=t_end. Routine titled
'set_initial_conditions' defines the starting values for r and v.

The arguments for each routine are provided after definition of each
routine. The returned values for the energies are scalars. The return
values for routine 'dervis' is an array with the two dimensional
derivitive for r in the first indices and for v in the last two indices.
Routine 'integrate_orbit' returns arrays for time, x and y positions,
and all the energies, every step of the interval. Routine
'set_initial_conditions' returns an array with all four values, as well
as the initial values for the energy per mass unit and the period T.
"""

import numpy as np
from numpy.linalg import norm
# ode.py is your routine containing integrators
from ode import fEuler, rk2, rk4

# use this to identify methods
integration_methods = {
    'Euler':fEuler,
    'RK2':rk2,
    'RK4':rk4
    }

# energies
def kinetic_energy(v):
    """
    Returns kinetic energy per unit mass: KE(v) = 0.5 v*v.

    Arguments
        v (array-like)
            velocity vector
    """
    return 0.5*np.dot(v,v)

def potential_energy(x,m):
    """
    Returns potential energy per unit mass: PE(x, m) = -m/norm(r)

    Arguments
        x (array-like)
            position vector
        m (scalar)
            total mass in normalized units
    """
    r = norm(x)
    return -m/r

def total_energy(z,m):
    """
    Returns energy per unit mass: E(z,m) = KE(v) + PE(x,m)

    Arguments
        z (numpy array)
            position and velocity numpy array [position, velocity]
        m (scalar)
            total mass in normalized units
    """
    # to break z into position, velocity vectors, we use array slices:
    # here z[n:m] means take elements of z with indices n <= j < m
    r = z[0:2]  # start with index 0 and take two indices: 0 and 1
    v = z[2:4]  # start with index 2 and take two indices: 2 and 3

    # replace the following two lines
    return potential_energy(r, m) + kinetic_energy(v)

def derivs(t,z,m):
    """
    Computes derivatives of position and velocity for Kepler's problem

    Arguments
        t (scalar)
            current time
        z (numpy array)
            position and velocity numpy array [position, velocity]
        m (scalar)
            total mass in normalized units
    Returns
        numpy array dzdt with components [ dx/dt, dy/dt, dv_x/dt, dv_y/dt ]
    """
    # Fill in the following steps
    # 1. split z into position vector and velocity vector (see total_energy for example)

    r = z[0:2]
    v = z[2:4]

    # 2. compute the norm of position vector, and use it to compute the force
    r_norm = norm(r)

    # 3. compute drdt (array [dx/dt, dy/dt])
    drdt = v
    # 4. compute dvdt (array [dvx/dt, dvy/dt])
    dvdt = -m/r_norm**3*r
    # join the arrays
    dzdt = np.concatenate((drdt,dvdt))
    return dzdt

def integrate_orbit(z0,m,tend,h,method='RK4'):
    """
    Integrates orbit starting from an initial position and velocity from t = 0
    to t = tend.

    Arguments:
        z0 (numpy array)
            inital position and velocity array

        m (scalar)
            total normalized mass of the system

        tend (scalar)
            final time of the model

        h (scalar)
            size of the time step

        method ('Euler', 'RK2', or 'RK4')
            identifies which stepper routine to use (default: 'RK4')

    Returns
        ts, Xs, Ys, KEs, PEs, TEs := arrays of time, x postions, y positions,
        and energies (kin., pot., total)
    """

    # set the initial time and phase space array
    t = 0.0
    z = z0

    # expected number of steps
    Nsteps = int(tend/h)+1

    # arrays holding t, x, y, kinetic energy, potential energy, and total energy
    ts = np.zeros(Nsteps)
    Xs = np.zeros(Nsteps)
    Ys = np.zeros(Nsteps)
    KEs = np.zeros(Nsteps)
    PEs = np.zeros(Nsteps)
    TEs = np.zeros(Nsteps)

    # store the initial point
    ts[0] = t
    Xs[0] = z[0]
    Ys[0] = z[1]
    # now extend this with KEs[0], PEs[0], TEs[0]
    KEs[0] = kinetic_energy(z[2:4])
    PEs[0] = potential_energy(z[0:2], m)
    TEs[0] = total_energy(z, m)
    # select the stepping method
    advance_one_step = integration_methods[method]
    # run through the steps
    for step in range(1,Nsteps):
        z = advance_one_step(derivs,t,z,h,args=m)
        # insert statement here to increment t by the stepsize h
        t += h
        # store values
        ts[step] = t
        # fill in with assignments for Xs, Ys, KEs, PEs, TEs
        Xs[step] = z[0]
        Ys[step] = z[1]

        KEs[step] = kinetic_energy(z[2:4])
        PEs[step] = potential_energy(z[0:2], m)
        TEs[step] = total_energy(z, m)

    return ts, Xs, Ys, KEs, PEs, TEs

def set_initial_conditions(a, m, e):
    """
    set the initial conditions for the orbit.  The orientation of the orbit is
    chosen so that y0 = 0.0 and vx0 = 0.0.

    Arguments
        a
            semi-major axis in AU
        m
            total mass in Msun
        e
            eccentricity ( x0 = (1+e)*a )

    Returns:
    x0, y0, vx0, vy0, eps0, Tperiod := initial position and velocity, energy,
        and period
    """

    # fill in the following lines with the correct formulae
    # total energy per unit mass
    eps0 = -1*m/(2*a)
    # period of motion
    Tperiod = np.pi/np.sqrt(2) *m * abs(eps0)**(-3/2)

    # initial position
    # fill in the following lines with the correct formulae
    x0 = (1+e)*a
    y0 = 0.0

    # initial velocity is in y-direction; we compute it from the energy
    # fill in the following lines with the correct formulae
    vx0 = 0.0
    vy0 = np.sqrt(2*eps0 + 2*m/x0)

    return np.array([x0,y0,vx0,vy0]), eps0, Tperiod
