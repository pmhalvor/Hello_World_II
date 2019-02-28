########################################################################
# Team armadillos: Cameron B, Brendan B, Trevor F, Per H
# AST304, Fall 2018
# Michigan State University
#
# Calculates and outputs a table of pressures and desnities for different
# masses ranging from 0.1 to 1 Solar Mass.
########################################################################
import astro_const as ac
from structure import pressure_guess, integrate
import numpy as np
from scipy.optimize import brentq
from eos import density
import matplotlib.pyplot as plt
import observations as observe
#from runner import filename

#set array of masses to calculate and other small parameters
mass_array = np.arange(0.1, 1.1, .1)*ac.Msun

delm = 0.0001
eta = 1e-10
xi = 0.05
mue = 2


#function used to find right Pressure guess
def mass_err(P_guess, M_want, delm, eta, xi, mue):
    """
    Computes how far off from the wanted Mass you are
    for a given central Pressure guess

    Arguments
        P_guess
            Central Pressure guess
        M_want
            Mass wanted
        delm
            initial offset from center (units = kg)
        eta
            The integration stops when P < eta * Pc
        xi
            The stepsize is set to be xi*min(p/|dp/dm|, r/|dr/dm|)
        mue
            mean electron mass

    Returns
        err
            Difference in wanted Mass and Mass calucluated from P_guess
    """
    M, rs, ps, = integrate(P_guess, delm, eta, xi, mue)
    err = M[-1] - M_want
    return err

table = np.ndarray((len(mass_array), 6))
for i in range(len(mass_array)):
    mass = mass_array[i]

    #get the upper and lower bounds on the central pressure
    Pguess_low = pressure_guess(mass*.9, mue)
    Pguess_high = pressure_guess(mass*1.1, mue)

    #get the Central Pressure for this mass
    P_central = brentq(mass_err, Pguess_low, 
                       Pguess_high, args=(mass, delm, eta, xi, mue))

    #run integration loop to calculate Mass, Radius & Pressure throughout star
    ms, rs, ps = integrate(P_central, delm, eta, xi, mue)

    #Define radius and central pressure
    R = rs[-1]
    rho_c = density(ps[0], mue)
    row = np.array([mass/ac.Msun, R/ac.Rsun, P_central, 
                    P_central*R**4/(ac.G*mass**2), rho_c, 
                    rho_c*4*np.pi*R**3/3/mass])
    table[i, :] = row

#Print out the table
print('M/M_sun\t\tR/R_sun\t\tPc (MKS)\t\t  alpha\t\t  rho_c\t\t\t  beta')
print('------------------------------------------------------------------\
      -------------------------------------')
for row in table:
    line=''
    for i in range(6):
        if row[i] > 1e5:
            line += '{:7.3e}\t\t'.format(row[i])
        else:
            line += '{:7.3f}\t\t'.format(row[i])

    print(line)

# 2.8
# plotting the mass vs radius of the above table
#
obs = observe.MassRadiusObservations()

plt.figure(1)
plt.plot(table[:,0],table[:,1]/0.01, '-o', label = "Model")
plt.errorbar(obs.mass,obs.radius,yerr=obs.radius_err,\
    xerr=obs.mass_err,fmt='ko',markersize=4, label ="Observed")

#plt.plot(filename[:,2,filename[:,4]]) #need to convert this all to non strings
plt.xlim(0, 1.1)
plt.ylim(0, 3)

plt.title('Normalized Mass vs Radius')
plt.xlabel('M/M_sun')
plt.ylabel(r'$R/(0.01\,R_\odot)$')

plt.legend()
plt.show()
