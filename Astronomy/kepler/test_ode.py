# unit test for integration methods
# do not alter this file

# our test problem is to integrate
#   dz/dt = [ w*z[1], -w*z[0] ]
# with initial conditions
#   z(t=0) = [ 0.0, 1.0 ].
# The solution is z = [ sin(w*t), cos(w*t) ].  For this test, we set
# w = 2*pi, and integrate from t = 0 to t = 2.
#

import numpy as np
from ode import fEuler, rk2, rk4

integration_methods = {
        'Euler': fEuler,
        'RK2': rk2,
        'RK4': rk4
        }

def f(t,z,w):
    """
    function returning RHS of our ODE.
    
    Arguments
        t (scalar)
        z (2 dimensional array)            
        w (scalar)
    Returns
        dzdt (2-D numpy array)
    """
    dzdt = np.zeros_like(z)
    dzdt[0] =  w*z[1]
    dzdt[1] = -w*z[0]
    return dzdt

def soln(t,w):
    """
    returns analytical solution of ODE
    Arguments
        t (scalar or array-like)
            independent variable
        w (scalar)
            parameter in system of ODEs
    Returns
        2-d solution array at times in argument t
    """
    return np.array([np.sin(w*t),np.cos(w*t)])

def do_one(method):
    # set initial conditions
    z = np.zeros(2)
    z[1] = 1.0

    # period is 1.0, frequency is 2*pi, stepsize is 1/100 of a period
    P = 1.0
    w = 2.0*np.pi/P
    h = P/100.0

    # we'll integrate from t = 0 to t = t_f = 2*P
    t = 0.0
    t_f = 2*P
    # Number of steps
    N = int(t_f/h)

    # check everything!
    print('integrating from t = {0} to t = {1} with {2} steps; h = {3:5.3f}\n'.\
        format(t,t_f,N,h))
    
    # print every 5th line
    PRINT_INTERVAL = 5
    # counter for steps
    cnt = 0
    # format for outputing results
    fmt = '{0:5d}{1:7.3f}   {2:7.3f}{3:7.3f}{4:9.2e}   {5:7.3f}{6:7.3f}{7:9.2e}'
    # format for header
    head_fmt = '{0:>5s}{1:>7s}   {2:>7s}{3:>7s}{4:>9s}   {5:>7s}{6:>7s}{7:>9s}'
    print(head_fmt.format(
        'step','t','z0','s0','|z0-s0|','z1','s1','|z1-s1|')
    )
    stepper = integration_methods[method]
    for step in range(N):
        z = stepper(f,t,z,h,args=w)
        t += h
        cnt += 1
        if (cnt % PRINT_INTERVAL == 0):
            zs = soln(t,w)
            resid = np.abs(z-zs)
            print(fmt.format(cnt,t,z[0],zs[0],resid[0],z[1],zs[1],resid[1]))

print('\n====================Forward Euler====================')
do_one('Euler')
print('\n================2nd order Runge-Kutta================')
do_one('RK2')
print('\n================4th order Runge-Kutta================')
do_one('RK4')
