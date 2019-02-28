#This will run all the files properly to make life easy
import structure as s
import astro_const as ac
import matplotlib.pyplot as plt
import pandas as pd


############### Constants #########################

delm = 0.1
eta = 1e-10
xi = 0.2
mue = 2

###################################################

### Setting up for subplot
f, (ax1, ax2) = plt.subplots(2, sharex=True)

### Setting up for table

lines=['source     |inst    |M low     |M high    |P low     |P high']
lines.append("______________________________________________________________")



filename = "Joyce.txt"
file = open(filename, "r")
counter = 0
for line in file:
    counter+=1
    if(counter>6):
        name = line[:10]
        instrument = line[16:22]
        R = float(line[28:33])
        R_error = float(line[36:41])
        M = float(line[48:53])
        M_error = float(line[56:61])
        M_high = M + M_error
        M_low = M - M_error

        Pc_low = s.pressure_guess(ac.Msun*M_low, mue)
        Pc_high = s.pressure_guess(ac.Msun*M_high, mue)


        ms_low, rs_low, ps_low= s.integrate(Pc_low, delm, eta, xi, mue)
        ms_high, rs_high, ps_high= s.integrate(Pc_high, delm, eta, xi, mue)
        Rs_low = rs_low/ac.Rsun
        Rs_high = rs_high/ac.Rsun

        ########### Plot mass vs radius for current star ############
        ax1.plot(Rs_low, ms_low/ac.Msun, label=name)
        ax1.set_title("Mass and Pressure vs Radius")
        ax1.set_ylabel("Mass (Solar Masses)")
        #plt.xlabel("Radius (Solar radius)")


        ax2.plot(Rs_high, ps_high, label = name)
        #ax2.set_title("Pressure vs Radius")
        ax2.set_xlabel("Radius (Solar radius)")
        ax2.set_ylabel("Pressure (MKS)")


        ####################### Table ##############################

        lines.append('{:10s} |{:4s}  |{:6f}  |{:6f}  |{:8.3e}  |{:8.3e}\
                     '.format(name, instrument, ms_low[-1]/ac.Msun,
                     ms_high[-1]/ac.Msun, ps_low[0], ps_high[0]))
        #lines.append('{:6f}'.format(ms_low[-1]/ac.Msun))
        #print(R, " ", R_error, " ", M, " ", M_error)

plt.legend(loc='best', bbox_to_anchor=(1.05, 2.2),
          ncol=1)
plt.show()
for i in lines:
    print(i)