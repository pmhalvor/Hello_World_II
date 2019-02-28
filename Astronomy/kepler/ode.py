########################################################################
# Armadillos, Cameron Blochwitz, Brendan Boyd, Trevor Franklin, Per Halvorsen
# AST 304, Fall 2018
# Michigan State University
########################################################################

"""
This is a series of algorithims that are able to numerically calculate our Systems
of ODEs
"""

# all routines that take a single step should have the same interface
def fEuler(f,t,z,h,args=()):
    """
    This is a Forward Euler Method. It takes in a given fuction and derivitive and takes 1 step

    Arguments
        f(t,z,...)
            function that contains the RHS of the equation dz/dt = f(t,z,...)

        t (scalar)
            time at current step

        z (numpy array)
            position and velocity values at current step

        h (scalar)
            step length

        args (tuple, optional)
            additional arguments to pass to f

    Returns
        znew = z(t+h)
    """

    # The following trick allows us to pass additional parameters to f
    # first we make sure that args is of type tuple; if not, we make it into
    # that form
    if not isinstance(args,tuple):
        args = (args,)

    # when we call f, we use *args to pass it as a list of parameters.
    # for example, if elsewhere we define f like
    # def f(t,z,x,y):
    #    ...
    # then we would call this routine as
    # znew = fEuler(f,t,z,h,args=(x,y))
    #
    return z + h*f(t,z,*args)

# You will need to flesh out the following routines for a second-order
# Runge-Kutta step and a fourth order Runge-Kutta step.

def rk2(f,t,z,h,args=()):
    """
    This is the Runge-Kutta 2nd Order method. It only calcuates 1 step.

    Arguments
        f(t,z,...)
            function that contains the RHS of the equation dz/dt = f(t,z,...)

        t (scalar)
            time at current step

        z (numpy array)
            position and velocity values at current step

        h (scalar)
            step length

        args (tuple, optional)
            additional arguments to pass to f

    Returns
        znew = z(t+h)
    """

    if not isinstance(args,tuple):
        args = (args,)

    # delete the line "pass" when you put in the full routine
    z_midpoint = z + h/2*f(t, z, *args)

    return z + h*f(t + h/2, z_midpoint, *args)

def rk4(f,t,z,h,args=()):
    """
    This is the Runge-Kutta 4th Order method. It only calcuates 1 step.

    Arguments
        f(t,z,...)
            function that contains the RHS of the equation dz/dt = f(t,z,...)

        t (scalar)
            time at current step

        z (numpy array)
            position and velocity values at current step

        h (scalar)
            step length

        args (tuple, optional)
            additional arguments to pass to f

    Returns
        znew = z(t+h)
    """

    if not isinstance(args,tuple):
        args = (args,)

    # delete the line "pass" when you put in the full routine
    z_midpoint1 = z + h/2*f(t, z, *args)
    z_midpoint2 = z + h/2*f(t+h/2, z_midpoint1, *args)
    z_p = z + h*f(t+h/2, z_midpoint2, *args)

    return z + h/6*(f(t, z, *args)         \
    + 2*f(t +h/2, z_midpoint1, *args)      \
    + 2*f(t+h/2, z_midpoint2, *args)       \
    + f(t+h, z_p, *args))
