Kepler
======

Project directory for comparison of ODE solvers and usage of the solvers to integrate orbits of two point particles (Kepler's problem). A description of the integration methods, Kepler's problem, and instructions for completing this project is available on D2L.

Contents of this directory
--------------------------

* `README.md`  
This file

* `ode.py`  
Routines to advance solution by one timestep

* `kepler.py`  
Routines to integrate orbits and compute energies

* `error.py`
This is the file that we use to calculate the errors in our functions and plot them.


Report/closeout
---------------



**Report 1**

***Quick bullet points for each step***

**1.** For this step we added the systems of ode for RK2 and RK4 into the given code.

**2.** We inputed the equations that describe the total energy into the kepler.py. This includes kinetic plus potential which equals the total energy of kelper's laws. When then added a derivative function that input time, velocity and position and the (normalized) point mass. Next we took the previous inputs and put them into a function that mapped out the orbit given the data. Lastly we created a function that defined our initial conditions for all of our inputs.

**3.** We modified the code so that it could pull the three different methods for solving Kelper's problem. This was inside the kelper.py file where we added the code to integrate the orbit and the energy of the orbit.

**4.** For this step we integrated the three methods (Euler, RK2, RK4) over three orbital periods. We then graphed the error in each. This showed that the RK4 method had the least amount of errors the smaller the time step went up, which is what we expected. When graphing Euler forward, RK2, and RK4, we used a logarithmic plot in order to best show the results.

**5.** As we increase the step size, all the orbits close down to an elliptical orbit. All of our methods closed onto having the semi major axis on the right side fitting in with the standard for an elliptical orbit.


**Analysis**

The goal of this assignment was implement three versions of code in order to map the orbital trajectories and energies of a two point mass system. We were given pseudo code along with a sample result with which to compare our own code output with. We were asked to map out the error on each method of coding and had to determine which was the most efficient way to map the system.

The first way we coded was using the Euler method. Mathematically this method maps out functions by taking derivative of the function at the first point and using that derivative as a "best guess" for where the line will extend out to. We used Euler over several step sizes and found that at larger step sizes, it tended to approximate the given function quite inaccurately.

Next we used the RK2 method for coding our two point system. This method takes the midpoint of our step and calculates the derivative of the function there. It is done this way because the midpoints of each step can approximate a curve much more efficiently than the Euler method. Using this method we were able to ascertain accurate results much more quickly.

Last we used the RK4 method. This method takes the weighted average of several midpoints along the curve and uses the weight of each one to "draw" out a curve that most accurately describes the given function in comparison to the other methods.

***Our Findings***

Using the three methods we mapped out three orbital periods of a two point mass system at a variety of step sizes to gain insight on to which method gave us the most accurate results the fastest. We mapped out the error in each method as well to better ascertain our results. Our error results were given in this graph below.

![](/error.png)

From this graph you can see that the error for the Euler at the largest time step was the most accurate, however its accuracy did not improve much as we decreased the step size, staying at a pretty consistent error value. This was not the case with the RK2 and RK4 however, showing a dramatic decrease in error as the step size lowered. While RK2 bottomed out at an error value around roughly 10 to the first, RK4's error decreased during the entirety of our decreasing step size. This accuracy is reflected in our orbital graphs for each method as seen below.

For our Euler method the accuracy was very much off in the beginning but did decrease to a decent elliptical orbit at the smallest step size, however there is still a slight eccentricity in its orbit.

![](/euler_traject.png)

With the other two methods, RK2 and RK4, both start out with a rougher looking orbit but coalesce to a more accurate ellipse with RK4 taking a almost unnoticeable difference in accuracy.

![](/rk2_traject.png)
![](/rk4_traject.png)

We theorize that had we let the RK4 run at an even smaller step size it would have garnered a much more accurate representation of the Kepler system orbit. For the intents of this project though, at the smallest step size that we were given to run, the three methods used were pretty close to each other for accuracy. Near the end, you can see euler becoming more and more inaccurate as the Total Energy begins to increase

![](/energy_euler_small_steps.png)
![](/energy_rk2_small_steps.png)
![](/energy_rk4_small_steps.png)

As shown, the plots for the smallest steps energies were very close to each other, but this was not the case for the largest time step energies as shown below.

![](/energy_euler_large_steps.png)
![](/energy_rk2_large_steps.png)
![](/energy_rk4_large_steps.png)

With such a large time step, the Total Energy quickly goes wild and does not stay constant like with a smaller step size.


Resources
---------
Coding standards are posted on D2L.
