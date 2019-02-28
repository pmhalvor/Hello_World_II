from structure import *
import astro_const as ac

import matplotlib.pyplot as plt

delm = 0.0001
eta = 1e-10
xi = 0.05
mue = 2

Pc_low = pressure_guess(ac.Msun*.1, mue)
Pc_high = pressure_guess(ac.Msun, mue)


ms_low, rs_low, ps_low= integrate(Pc_low, delm, eta, xi, mue)
ms_high, rs_high, ps_high= integrate(Pc_high, delm, eta, xi, mue)

plt.plot(rs_low/ac.Rsun, ms_low/ac.Msun)
plt.title("Mass vs Radius for .1 Solar")

plt.ylabel("Mass (Solar Masses)")
plt.xlabel("Radius (Solar radius)")
plt.show()

plt.plot(rs_high/ac.Rsun, ms_high/ac.Msun)
plt.title("Mass vs Radius for 1 Solar")

plt.ylabel("Mass (Solar Masses)")
plt.xlabel("Radius (Solar radius)")
plt.show()

const_term_low = ps_low[0]*rs_low[-1]**4/ms_low[-1]**2
const_term_high = ps_high[0]*rs_high[-1]**4/ms_high[-1]**2

print(const_term_low, const_term_high)
"""
plt.plot(Rs, ps)
plt.title("Pressure vs Radius")
plt.xlabel("Radius (Solar radius)")
plt.ylabel("Pressure (??)")
plt.show()
"""
