###########################################################################
# Team armadillos: Cameron B, Brendan B, Trevor F, Per H
# AST304, Fall 2018
# Michigan State University
#
# Calculates and Plots Luminosity vs Effective Temperature and central
#Densty vs Central Temperature for Low mass stars. (0.1 to 0.3 solar Masses)
############################################################################
import numpy as np
from structure import integrate, mean_molecular_weight, central_values
from rad_finder import radius_finder
from astro_const import Rsun, Msun, Lsun
from Teff import Teff
import matplotlib.pyplot as plt


mu = mean_molecular_weight()
delta_m = 1e-9
eta = 1e-14
xi = 0.05
weak_fac = 1

Msolar = np.linspace(0.1, 0.3, 20)

Ms = Msolar*Msun
Lums = []
Temps = []
cTemps = []
cRhos = []
Rguess = 0.25*Rsun

for M in Ms:
    #find appropriate radius for Mass
    R = radius_finder(M, Rguess, mu, delta_m, eta, xi)

    #calculate central values
    z, rho_c, Tc = central_values(M, R, delta_m, mu, weak_fac)

    #calculate values throughout star
    m, r, p, l = integrate(M, R, mu, delta_m, eta, xi, weak_factor = weak_fac, max_steps = int(1e5))

    L = l[-1]/Lsun
    T = Teff(M)

    #convert Density to cgs
    rho_c_cgs = rho_c/1000
    Lums.append(L)
    Temps.append(T)
    cTemps.append(Tc)
    cRhos.append(rho_c_cgs)

logTemps = np.log10(np.array(Temps))
logLums = np.log10(np.array(Lums))
logcTemps = np.log10(np.array(cTemps))
logcRhos = np.log10(np.array(cRhos))


#plot Luminosity vs Effective Temperature
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(logTemps, logLums, 'o--')

#plot Central Density vs Central Temp
ax2.plot(logcRhos, logcTemps,'o--')

# add text showing mass for each point
offset = 0.008
for i, mass in enumerate(Msolar):
    if not i%3:
        ax1.annotate("{:.2f} ".format(mass)+r"$M_{\odot}$", (logTemps[i], logLums[i]+offset))
        ax2.annotate("{:.2f} ".format(mass)+r"$M_{\odot}$", (logcRhos[i], logcTemps[i]+offset))
#invert axis and add labels
ax1.invert_xaxis()
ax1.set_title("Luminosity vs Effevtive Temp for Low Mass Stars")
ax1.set_ylabel(r"$Log(L / {L_{\odot}})$")
ax1.set_xlabel(r"$Log(T_{eff} / {K})$")

ax2.set_title("Central Temp vs Central Density for Low Mass Stars")
ax2.set_xlabel(r"$Log(\rho_{c} / {g cm^{-3}})$")
ax2.set_ylabel(r"$Log(T_{c} / {K})$")
plt.show()

try:
    fig1.savefig("plots/LumVsTeff.png")
    fig2.savefig("plots/cDensityVsTemp.png")
except FileNotFoundError:
    print("####################################################\n\n")
    print("Failed to save plot. Make sure directory 'plots' exists\n\n")
    print("####################################################\n\n")
