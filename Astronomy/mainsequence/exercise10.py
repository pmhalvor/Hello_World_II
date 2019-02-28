########################################################################
# Team armadillos: Cameron B, Brendan B, Trevor F, Per H
# AST304, Fall 2018
# Michigan State University
#
# makes plots of Temperature and Luminosity for 0.3 solar mass star
########################################################################
import numpy as np
from rad_finder import radius_finder
from structure import integrate, mean_molecular_weight, central_values
from Teff import Teff
from astro_const import Rsun, Msun, Lsun
from adiabat import adiabat
import matplotlib.pyplot as plt

#define counditions for integration
M = 0.3*Msun
Rguess = 0.35*Rsun
delta_m = 1e-9
eta = 1e-14
xi = 0.01
mu = mean_molecular_weight()

#find the right radius for this mass
R = radius_finder(M, Rguess, mu,delta_m, eta, xi)

#with mass and radius, find all vals throughout star
ms, rs, Ps, Ls = integrate(M, R, mu, delta_m, eta, xi, max_steps = int(1e6))

#calc some of the central values
z_c, rho_c, Tc = central_values(M, R, delta_m, mu, weak_factor = 1)
Pc = z_c[1]

#use central vals to find density and Temp throughout star
rhos, Ts = adiabat(Ps, Pc, rho_c, Tc)

#find when Luminosity is 90% max
Lum_percent = Ls/Ls[-1]
for i in range(len(Lum_percent)):
    if Lum_percent[i] >= 0.9:
        rad90lum = rs[i]
        mass90lum = ms[i]
        break

#create figure to hold plots
fig = plt.figure(1)
fig.suptitle("Star of {:.2f} ".format(M/Msun) +
             r"$M_{\odot}$ " +
             "and {:.2f} ".format(R/Rsun) +
             r"$R_{\odot}$")

#plot Temp vs Radius
fig.add_subplot(221)
plt.title("Temperature vs Radius")
plt.xlabel(r"$R / {R_{star}}$")
plt.ylabel(r"$T / {10^6} K$")
plt.plot(rs/R, Ts/1e6)

#plot Temp vs Mass
fig.add_subplot(222)
plt.title("Temperature vs Mass")
plt.xlabel(r"$M / {M_{star}}$")
plt.ylabel(r"$T/{10^6}K$")
plt.plot(ms/M, Ts/1e6)

#plot Lum vs Radius
fig.add_subplot(223)
plt.title("Luminosity vs Radius")
plt.xlabel(r"$R / {R_{star}}$")
plt.ylabel(r"$L/10^{24}W$")
plt.plot(rs/R, Ls/1e24)
plt.vlines(rad90lum/R, 0, 5, colors = 'r',
        linestyles='dashed',
        label = "90% Lum")
plt.legend()

#plot Lum vs Mass
fig.add_subplot(224)
plt.title("Luminosity vs Mass")
plt.xlabel(r"$M / {M_{star}}$")
plt.ylabel(r"$L/10^{24}W$")
plt.plot(ms/M, Ls/1e24)
plt.vlines(mass90lum/M, 0, 5, colors = 'r',
        linestyles='dashed',
        label = "90% Lum")
plt.legend()

#format subplot and then show
plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()

#save the plot as png
try:
    fig.savefig("plots/mass0.3_plots.png")
except FileNotFoundError:
    print("####################################################\n\n")
    print("Failed to save plot. Make sure directory 'plots' exists\n\n")
    print("####################################################\n\n")

#report 90% Lum mark
print("When Luminosity hits 90% of its Final Value")
print("Radius: {:.2f} solar radius. {:.1f}% of total Radius".format(rad90lum/Rsun, rad90lum/R*100))
print("Mass enclosed: {:.1f}% of total mass".format(mass90lum/M*100))
