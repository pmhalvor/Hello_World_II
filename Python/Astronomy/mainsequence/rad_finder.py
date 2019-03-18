########################################################################
# Team armadillos: Cameron B, Brendan B, Trevor F, Per H
# AST304, Fall 2018
# Michigan State University
#
# Finds the right radius where the Nuclear luminosity is equal to
# the luminosity found from effective Temperature
########################################################################
from scipy.optimize import brentq
import numpy as np
from Teff import Teff
from structure import integrate, mean_molecular_weight
from astro_const import sigmaSB, Msun, Rsun, Lsun
import matplotlib.pyplot as plt

def calc_lum(R, M, mu, delta_m, eta, xi, w_fac =1):
    ms, rs, Ps, Ls = integrate(M, R, mu, delta_m, eta, xi, weak_factor = w_fac,  max_steps = int(1e6))

    return Ls[-1] - 4*np.pi*R**2 * sigmaSB * Teff(M)**4

def radius_finder(M, Rguess, mu, delta_m, eta, xi):
    delta = 5
    R = brentq(calc_lum, Rguess/delta, Rguess*delta, args=(M, mu, delta_m, eta, xi),xtol=1e-6 )

    return R

if __name__ == '__main__':

    delta_m = 1e-8
    eta = 1e-10
    xi = 0.005
    mu = mean_molecular_weight()
    print("0.3 Solar mass")
    print("guess .3 solar radius")
    M = 0.3*Msun
    Rg = 0.3*Rsun

    R = radius_finder(M, Rg, mu, delta_m, eta, xi)

    print("Right R/Rsun is ", R/Rsun)

    ms, rs, Ps, Ls = integrate(M, R, mu, delta_m, eta, xi,  max_steps = int(1e6))
