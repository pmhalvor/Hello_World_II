########################################################################
# Team Armadillos: Cameron B, Brendan B, Trevor F, Per H
# AST304, Fall 2018
# Michigan State University
#
# This file contains the functions that define our density and the pressure
# of the stars.
#
# Our pressure equation takes in the mass density, mue, and
# returns the pressure exerted by electrons on each other for the pressure
# of a white dwarf.
#
# Our density equation pulls in the electron pressure and mue to return the
# mass density varying by the pressure.
########################################################################

# import/define constants here
import astro_const as ac
import numpy as np


def pressure(rho, mue):
    """
    Arguments
        rho
            mass density (kg/m**3)
        mue
            baryon/electron ratio

    Returns
        electron degeneracy pressure (Pascal)
    """

    #K_e is a constant defined in astro_const.py
    p = ac.K_e*(rho/mue)**(5./3.)
    return p

def density(p, mue):
    """
    Arguments
        p
            electron degeneracy pressure (Pascal)
        mue
            baryon/electron ratio

    Returns
        mass density (kg/m**3)
    """

    # replace following lines with body of routine
    rho = mue*ac.m_u*(5*p*(8.*np.pi/3.)**(2/3) * ac.m_e/ac.h**2)**(3/5)
    return rho
