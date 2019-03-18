########################################################################
# Team armadillos: Cameron B, Brendan B, Trevor F, Per H
# AST304, Fall 2018
# Michigan State University
#
# <description of module>
########################################################################

import numpy as np
from eos import density, pressure
from ode import rk4
import astro_const as ac

def stellar_derivatives(m,z,mue):
    """
    RHS of Lagrangian differential equations for radius and pressure

    Arguments
        m
            current value of the mass
        z (array)
            current values of (radius, pressure)

    Returns
        dzdm (array)
            Lagrangian derivatives dr/dm, dP/dm

    dr/dm = 1/(4*np.pi*(z[0]**2)*density(z[1], mue))
    dP/dm = - (ac.G*m)/(4*np.pi*z[0]**4)
    """

    dzdm = np.zeros_like(z)
    dzdm[0] = 1/(4*np.pi*(z[0]**2)*density(z[1], mue))
    dzdm[1] = - (ac.G*m)/(4*np.pi*z[0]**4)

    #pass
    return dzdm

def central_values(Pc,delta_m,mue):
    """
    Constructs the boundary conditions at the edge of a small, constant density
    core of mass delta_m with central pressure P_c

    Arguments
        Pc
            central pressure (units = MKS)
        delta_m
            core mass (units = Solar Masses)
        mue
            nucleon/electron ratio (unitless)

    Returns
        z = array([ r, P ])
            central values of radius and pressure (units = [Solar radii, MKS])

    """
    z = np.zeros(2)
    # compute initial values of z = [ r, P ]
    z[0] = (3*delta_m/(4*np.pi*density(Pc, mue)))**(1/3)
    z[1] = Pc
    return z

def lengthscales(m,z,mue):
    """
    Computes the radial length scale H_r and the pressure length H_P

    Arguments
        m
            current mass coordinate (units = Solar Masses)
        z (array)
           [ r, P ] (units = [Solar Radii, MKS])
        mue
            mean electron weight (unitless)

    Returns
        HR, HP (units = Solar Radii and MKS)
    """
    # fill this in
    HR = 4*np.pi*z[0]**3*(density(z[1], mue))
    HP = 4*np.pi*z[0]**4*z[1]/(ac.G*m)
    return HR, HP

def integrate(Pc,delta_m,eta,xi,mue,max_steps=10000):
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
            The stepsize is set to be xi*min(p/|dp/dm|, r/|dr/dm|)
        mue
            mean electron mass
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
    p_step = np.zeros(max_steps)

    curr_m = delta_m
    z = central_values(Pc, delta_m, mue)

    Nsteps = 0
    for step in range(max_steps):
        # check for completion
        if (z[1] < eta*Pc):
            break
        # store the step
        m_step[step] = curr_m
        r_step[step] = z[0]
        p_step[step] = z[1]
        # set the stepsize
        HR, HP = lengthscales(curr_m, z, mue)
        h = xi*min(HR,HP)
        # take a step
        curr_m += h
        z = rk4(stellar_derivatives, curr_m, z, h, mue)
        # increment the counter
        Nsteps += 1
    # if the loop runs to max_steps, then produce an error
    else:
        Nsteps = max_steps
        raise Exception('too many iterations')

    return m_step[0:Nsteps],r_step[0:Nsteps],p_step[0:Nsteps]

def pressure_guess(m,mue):
    """
    Computes a guess for the central pressure based on virial theorem and mass-
    radius relation.

    Arguments
        m
            mass of white dwarf (units = kg)
        mue
            mean electron mass (unitless)

    Returns
        P
            guess for pressure (units = kg/m**3)
    """
    # fill this in
    Pguess = ac.G**5/ac.K_e**4 * (m*0.35*mue**2)**(10/3)
    return Pguess
