########################################################################
# Team armadillos: Cameron B, Brendan B, Trevor F, Per H
# AST304, Fall 2018
# Michigan State University
#
# calculates the nuclear rate of hydrogen
########################################################################
from numpy import exp
def epsilon_nuc(rho, T, H_frac=0.706, weak_fac=1):
    """
    Computes the nuclear rate for a given density and temperature

    Arguments
        rho
            Current Density (Pa)
        T
            Current Temperature (K)
        H_frac
            Fraction of Hydrogen in the star
        weak_fac
            Factor that increases the weak force
    Returns
        nuc_rate
            The rate of nuclear reaction (W/kg)
    """

    Tg = T/1e9

    nuc_rate = 2.4e-3 * rho * H_frac**2 *weak_fac* Tg**(-2/3) * exp(-3.380*Tg**(-1/3))

    return nuc_rate


#unit test
