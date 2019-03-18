########################################################################
# Team armadillos: Cameron B, Brendan B, Trevor F, Per H
# AST304, Fall 2018
# Michigan State University
#
# <description of module>
########################################################################

import numpy as np
from ode import rk4
import astro_const as ac
from nuc_rate import epsilon_nuc
from adiabat import adiabat

def stellar_derivatives(m,z, rho, T, weak_factor):
    """
    RHS of Lagrangian differential equations for radius and pressure

    Arguments
        m
            current value of the mass (kg)
        z (array)
            current values of (radius, pressure, luminosity)
        T
            current Temperature (K)
    Returns
        dzdm (array)
            Lagrangian derivatives dr/dm, dP/dm, dL/dm

    """

    dzdm = np.zeros_like(z)
    dzdm[0] = 1/(4*np.pi*(z[0]**2)*rho)
    dzdm[1] = - (ac.G*m)/(4*np.pi*z[0]**4)
    dzdm[2] = epsilon_nuc(rho, T, weak_factor)

    return dzdm

def central_values(M, R, delta_m, mu, weak_factor):
    """
    Constructs the boundary conditions at the edge of a small, constant density
    core of mass delta_m with central pressure P_c

    Arguments
        Pc
            central pressure (units = Pa)
        delta_m
            core mass (units = kg)

    Returns
        z = array([ r, P, L ])
            central values of radius, pressure and luminosity
             (units = [m, Pa, W])
        rho_c
            central density value (kg/m^3)
        Tc
            central temperature (K)
    """
    z = np.zeros(3)
    # compute initial values of z = [ r, P ]
    rho_c = 5.99*3*M/(4*np.pi*R**3)
    Pc = 0.77*ac.G*M**2/R**4
    Tc = 0.54* mu*ac.m_u/ac.k * ac.G*M/R

    z[0] = (3*delta_m/(4*np.pi*rho_c))**(1/3)
    z[1] = Pc
    z[2] = epsilon_nuc(rho_c, Tc, weak_factor)*delta_m
    return z, rho_c, Tc

def lengthscales(m,z, rho, T, weak_factor):
    """
    Computes the radial length scale H_r and the pressure length H_P

    Arguments
        m
            current mass coordinate (units = kg)
        z (array)
           [ r, P, L] (units = [m, Pa, W])
        T
            Current Temperature (K)

    Returns
        lengthscales for r, P, L
    """
    dzdm = stellar_derivatives(m, z,rho, T, weak_factor) + 1e-30

    return z/np.abs(dzdm)

def integrate(M,R,mu,delta_m,eta,xi, weak_factor = 1,max_steps=10000):
    """
    Integrates the scaled stellar structure equations

    Arguments
        Pc
            central pressure (units = MKS)
        delta_m
            initial offset from center (units = Solar Masses)
        eta
            The integration stops when P < eta * Pc
        xi
            The stepsize is set to be xi*min(p/|dp/dm|, r/|dr/dm|, L/|dL/dm|)
        weak_factor
            the

        max_steps
            solver will quit and throw error if this more than max_steps are
            required (default is 10000)

    Returns
        m_step, r_step, p_step
            arrays containing mass coordinates, radii and pressures during
            integration (m_step units = Solar Masses,
            r_step units = Solar Radii, p_step units = kg/m**3)
    """

    m_step = np.zeros(max_steps)
    r_step = np.zeros(max_steps)
    P_step = np.zeros(max_steps)
    L_step = np.zeros(max_steps)

    #calculate values at the center
    curr_m = delta_m

    z, rho_c, Tc = central_values(M, R, delta_m, mu, weak_factor)
    Pc = z[1]
    Nsteps = 0

    for step in range(max_steps):
        # check for completion
        if (z[1] < eta*Pc):
            break
        # store the step
        m_step[step] = curr_m
        r_step[step] = z[0]
        P_step[step] = z[1]
        L_step[step] = z[2]

        #calc Temperature
        rho, T = adiabat(z[1], Pc, rho_c, Tc)
        # set the stepsize
        HR, HP, HL = lengthscales(curr_m, z,rho, T, weak_factor)
        h = xi*min(HR,HP, HL)
        # take a step
        z = rk4(stellar_derivatives, curr_m, z, h, (rho, T, weak_factor))
        curr_m += h

        # increment the counter
        Nsteps += 1
    # if the loop runs to max_steps, then produce an error
    else:
        Nsteps = max_steps
        raise Exception('too many iterations')

    return m_step[:Nsteps],r_step[:Nsteps],P_step[:Nsteps], L_step[:Nsteps]

def mean_molecular_weight(H_frac=0.706, He_frac=0.275, N_frac=0.019):
    H_A = 1
    H_Z = 1
    He_A = 4
    He_Z = 2
    N_A = 14
    N_Z = 7

    return 1/(H_frac*(1 + H_Z)/H_A + He_frac*(1 + He_Z)/He_A + N_frac*(1 + N_Z)/N_A)
