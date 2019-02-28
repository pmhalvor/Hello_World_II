import numpy as np
from structure import integrate, mean_molecular_weight
from astro_const import Rsun, Msun, Lsun,G, sigmaSB


mu = mean_molecular_weight()
delta_m = 1e-9
eta = 1e-14
xi = 0.01

Mput = Msun*.3
Rput = Rsun*.33
m, r, p, l = integrate(Mput, Rput, mu, delta_m, eta, xi, max_steps = int(1e6))

M = m[-1]/Msun
R = r[-1]/Rsun
L = l[-1]/Lsun


print("mass = {}, r = {}, L = {}".format(M, R, L))
errM = (Mput - m[-1])/Mput
errR = (Rput - r[-1])/Rput

print("mass err = {} rad err = {}".format(errM, errR))
