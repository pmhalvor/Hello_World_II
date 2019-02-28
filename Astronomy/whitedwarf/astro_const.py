########################################################################
# Team <armidillos>: <Bredan Boyd, Cameran Blochwitz, Per Halvorsen>
# AST304, Fall 2018
# Michigan State University
#
# Useful astrophysical constants
# Solar values were taken from the Particle Data Group,
# http://pdg.lbl.gov/2018/reviews/rpp2018-rev-astrophysical-constants.pdf
# The remaining are pulled in from scipy.constants
########################################################################

import scipy.constants as _sc
from numpy import pi
# solar mass, radius, luminosity
Msun = 1.98848e30 # kg
Rsun = 6.957e8 # m
Lsun = 3.828e26 # W

# physical constants from scipy, all in MKS units
G = _sc.G
h = _sc.h
hbar = _sc.hbar
m_e = _sc.m_e
m_p = _sc.m_p
m_n = _sc.m_n
m_u = _sc.m_u
c = _sc.c
k = _sc.k
pc = _sc.parsec
au = _sc.astronomical_unit
year = _sc.year
sigmaSB = _sc.sigma
K_e = (1/5)*(3/8/pi)**(2/3)*h**2/m_e/m_u**(5/3)

if __name__ == "__main__":

    constants = [
        ("solar mass",Msun,"kg"),
        ("solar radius",Rsun,"m"),
        ("solar luminosity",Lsun,"W"),
        ("gravitational constant",G,"m**3 s**-2 kg**-1"),
        ("Planck constant",h,"J s"),
        ("Planck constant, reduced",hbar,"J s"),
        ("electron mass",m_e,"kg"),
        ("proton mass",m_p,"kg"),
        ("neutron mass",m_n,"kg"),
        ("atomic mass unit",m_u,"kg"),
        ("speed of light",c,"m s**-1"),
        ("Boltzmann constant",k,"J K**-1"),
        ("parsec",pc,"m"),
        ("astronomical unit",au,"m"),
        ("year",year,"s"),
        ("Stefan-Boltzmann constant",sigmaSB,"W m**-2 K**-4")
    ]


    for const in constants:
        print('{0[0]:28} = {0[1]:11.4e} {0[2]}'.format(const))
