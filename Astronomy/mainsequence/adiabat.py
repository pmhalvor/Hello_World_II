import numpy as np
from structure import *
from astro_const import m_u, k, Msun, Rsun, G



def adiabat(P, Pc, rhoc, Tc):
    """
    Computes the density and temperature along an adiabat
    given the central pressure, density, and temperaure,
    as well as a the respective pressure

    Arguments
        P
            Pressure at which we want to find our rho and T
        Pc
            Central pressure
        rhoc
            Central density
        Tc
            Central temperature

    Returns
        rho
            density along adiabat at pressure P
        T
            Temperature along adiabat at pressure P
    """

    gamma = (5./3)
    rho = rhoc*(P/Pc)**(1/gamma)
    T = Tc*(P/Pc)**(1-(1/gamma))
    return rho, T


if __name__ == '__main__':
    M = Msun
    R = Rsun

    Pc = 0.77*(G*M**2)/R**4
    rhoc = 5.99*(3*M)/(4*np.pi*R**3)
    Tc = (mean_molecular_weight()*m_u/k)*(Pc/rhoc)

    Ps = np.linspace(10**-3, 10**0, 100)*Pc
    print("P            ", "rho*T*K/mu*m_u ", "diff")
    avg = 0
    for P in Ps:
        rho, T = adiabat(P, Pc, rhoc, Tc)
        P_ideal =  rho*T*k/(mean_molecular_weight()*m_u)
        diff = abs(P - P_ideal)/P
        print("{:10.5e}    {:10.5e}    {:.3e}".format(P, P_ideal, diff))
        avg+=diff

    print("The average relative difference is ", avg/100.)
