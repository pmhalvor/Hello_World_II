# unit test for equation of state
# do not alter this file

import numpy as np
from eos import pressure, density

def test_eos(pressure_func,density_func,mue=2.0,tolerance=1.0e-12,
        testfile='eos_table.txt',units='MKS'):
    """
    compares pressure and density functions against tabulated values

    Arguments
        pressure_func
            function that computes pressure given density and mue
        density_func
            function that computes density given pressure and mue
        mue
            baryon/electron ratio (default = 2.0)
        tolerance
            differences between computed and tabulated EOS values that are 
            larger than tolerance will trigger a warning (default = 1.0e-12)
        testfile
            table of density (kg/m**3), pressure (Pa), and Fermi energy 
            (electron rest mass-energy). Values computed by the eos module are              compared against this (default = 'eos_table.txt')
        units (either 'MKS' or 'CGS')
            specifies either MKS (default) or CGS units

    Returns
        True if all tests passed, False otherwise
    """

    accept = True
    
    # load data, ignoring column containing Fermi energy/(m_e c**2)
    data = np.loadtxt(testfile,skiprows=3,usecols=[0,1])
    density_val = data[:,0]
    pressure_val = data[:,1]

    # conversion factors if eos outputs cgs units
    density_mks_to_cgs = 1.0e-3
    pressure_mks_to_cgs = 10.0
    if units.lower()=='cgs':
        density_val *= density_mks_to_cgs
        pressure_val *= pressure_mks_to_cgs

    # table header
    print(
        '{0:>14}{1:>14}{2:>14}  {3:>14}{4:>14}{5:>14}\n'.format(
            'rho (table)','rho (test)','difference',
            'P (table)','P (test)','difference'))

    # iterate over density, pressure values and test individually
    for rho, p in zip(density_val, pressure_val):
        Ptest = pressure_func(rho,mue)
        rhotest = density_func(p,mue)
        Perr = (Ptest-p)/p
        rhoerr = (rhotest-rho)/rho
        print(
            '{0:14.6e}{1:14.6e}{2:14.6e}  {3:14.6e}{4:14.6e}{5:14.6e}'.\
            format(rho,rhotest,rhoerr,p,Ptest,Perr))

        if max(abs(Perr),abs(rhoerr)) > tolerance:
            print('******** value outside accepted tolerance ********\n')
            accept = False
            
    return accept


if __name__ == "__main__":

    print('Comparing EOS to eos_table.txt...\n')
    if (test_eos(pressure,density)):
        print('\nSUCCESS: all values within tolerance')
    else:
        print('\nFAIL')
