from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from astro_const import Msun

def Teff(M):
    """
    Computes the effective temperature for a given mass.
    Most accurate between 0.1 and 0.3 solar masses.
    (Optional: Plots are left in too see which method is better. To use just
    uncomment them.)

    Arguments
        M
            Mass relative to a sloar mass (M/Msun)

    Returns
        Teff
            Effective temperature for this mass
    """
    Ms = np.array([0.1, 0.15, 0.2, 0.3])*Msun
    Teffs = np.array([2800, 3150, 3300, 3400])
    #M_values = np.linspace(0.1, 0.4, 100)
    #Teffs_inter = np.interp(M_values, Ms, Teffs)
    #plt.plot(M_values, Teffs_inter, '-xy')

    #popt, pcov = curve_fit(func, Ms, Teffs)
    #plt.plot(M_values, func(M_values, *popt))
    #plt.plot(Ms, Teffs, 'go')
    #plt.title("Est. of T_eff (mass) for low mass stars")
    #plt.show()
    return np.interp(M, Ms, Teffs)#func(M, *popt)

#It looks like a logarithmic curve fits better than interpolation by numpy
def func(x, a, b, c):
    """
    General logarithmic curve for our curve_fit function

    Arguments
        x
            Numpy array for area to estimate
        a
            Coeffiecient
        b
            Parameter
        c
            Coeffiecient
    """
    return a*np.log(b+x)+c
