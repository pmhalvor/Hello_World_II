White Dwarf
===========

Project directory for a model of white dwarf. A full description of the project is available on D2L.

Contents
--------

1. `README.md`: this file
2. `mass_table.py` this is the main top level code of the project. Takes information from other file and uses them to plot
    the model's data and prints the table with all the relevent information
3.  `eos.py`: code defining the equations of state within the white dwarf itself
3. `test_eos.py`: unit test for the equation of state
4. `eos_table.txt`: comparison data for the equation of state, used by `test_eos.py`
5. `astro_const.py`: module containing useful constants. uses `scipy.contants`
6. `Joyce.txt`: observed masses and radii of white dwarfs, from Joyce et al. (2018)
7. `observations.py`: module for loading data in `Joyce.txt` and storing it in a lightweight class
8. `structure.py`: contains functions used for defining and integrating over the stellar structure.
9. `test_integration.py` code that tests the integration method and pressure guessing system
10. `ode.py` fuction used for integration via the Runge-Kutta 4 method.

Report/closeout
---------------

# EOS
We started our program off by setting up our eos.py file. Here we defined a function for density with respect to pressure and mu, and a function for pressure with respect to density and mu. To ensure that our functions were working properly, we ran the file test_eos.py, which was provided for us in our GitHub repository. Our result was a table of the expected and calculated values of both the densities and pressures, respectively, along with the differences between the expected and calculated values. Since all of our functions were within the tolerance for error, our function printed out a "Success!" message. The differences between the expected and calculated values were of a degree of 10^-16, which is well below the capable precision of our computers.

# Stellar Derivatives
For easier implementation of the boundary conditions and a more systematic approach to solving for the mass within a shell with radius r, we converted our equations for the structure of a star in steady states to Lagrangian form.

# Length scales
## How we chose our xi value:
 We started with a small guess of 0.1, as recommended in the exercise text, and plotted a Mass versus Radius relation to see how the change would look as we move from the inside of the star to the surface. This graph was quite jagged, so we decreased xi slightly, and plotted the same relation again. We continued decreasing xi and plotting the relation until we had a smooth plot, and our mass and radius was accurate to within 0.001 of the true mass and radius we desired. The important limitations here were runtime of our program for very small step sizes, and estimates within our desired tolerance for our mass and radius for large step sizes.


# Integration
## Starts
Since mass = 0 would cause problems, and not allow our ODE to start, we started instead with a sufficiently small mass = 0.0001, compared to the mass of the sun, to start with. We saw that the initial mass had little impact on the rest of the integration.

## Stops
The integration stops when we reach the max_steps (to prevent insanely long run times) or when we get about a pressure of 0. We measure this by calculating eta*Pressure_central. We choose eta to be 10^-10 and saw that adjusting didn't have significant impact on our final result so we kept it there.

# Calibration
## Xi
As stated above the main calibration we did with integration variables was looking at how xi impacted the final mass that we calculated.
## Pressure guesser
In addition we calibrated our pressure_guesser function by comparing a mass we estimated from our data to the mass corresponding to the central pressure. The mass we gave it was about 0.35*mass we got out. We then edited pressure guesser so that when you give it a mass, its pressure guess is fairly accurate. This is helpful later in our code because we could then search a smaller range for the true central pressure of a given mass, with could helped shorten the runtime of our final code.

# Finding our table values
## Finding correct central pressure for given mass
We made a function mass_err which takes in an estimated pressure, a given mass (between .1 to 1 solar mass), and gives us the error between the given mass, and the numerically calculated mass. We then used the brentq estimation method on this mass_err function, along with our calibrated upper and lower boundaries for our central pressure. The result of this process gave us a central temperature which, when plugged into mass_err, would be 0.
## Virial Relation
The columns in our table labeled "alpha" and "beta" check our results against the virial relation. These show us that our pressures and densities scale with mass correctly. Since we get the roughly same values for every inputted mass, we can conclude that our results coincide with the virial theorem.

# Plots and Tables

## Table 1:
This table shows the different total masses and radii of white dwarfs with masses ranging from .1 to 1 solar mass, along with their pressures and densities.

|M/M_sun  |       R/R_sun    |     Pc (MKS)       |           alpha   |        rho_c   |                beta |
|--:      |--:               |--:                 |--:                |--:             |--:                        |
 | 0.100     |      0.027|         1.921e+19|                 0.893|         4.679e+07|                  6.464|
  |0.200      |     0.021 |        1.936e+20 |                0.893 |        1.872e+08 |                6.464|
  |0.300       |    0.019  |       7.479e+20  |               0.893  |       4.211e+08  |               6.464|
  |0.400        |   0.017   |      1.951e+21   |              0.893   |      7.487e+08   |              6.464|
  |0.500         |  0.016    |     4.106e+21    |             0.894    |     1.170e+09    |             6.465|
  |0.600          | 0.015     |    7.538e+21     |            0.893     |    1.684e+09     |            6.464|
  |0.700         |  0.014      |   1.260e+22      |           0.893      |   2.293e+09      |           6.464|
  |0.800     |      0.013       |  1.967e+22       |          0.893       |  2.995e+09       |          6.464|
  |0.900      |     0.013    |     2.912e+22        |         0.893        | 3.790e+09        |         6.464|
  |1.000       |    0.012     |    4.138e+22         |        0.894         |4.679e+09         |        6.465|

## Plot 1
This plot shows the relationship of radii and masses of white dwarfs ranging from .1 to 1 solar mass, along with the data from the stars observed and recorded in the Joyce.txt file
![](https://github.com/MSU-AST304-FS2018/gcp2-white-dwarf-armadillos/blob/master/Screen%20Shot%202018-11-15%20at%2010.16.58%20AM.png)

## Plot 2
These were the first plots we created for this project to make sure we understood how the mass within a shell increases according to the radius of the shell. This provided a general understanding of the structure of white dwarfs.
![](https://github.com/MSU-AST304-FS2018/gcp2-white-dwarf-armadillos/blob/master/Screen%20Shot%202018-11-15%20at%2010.17.54%20AM.png)
![](https://github.com/MSU-AST304-FS2018/gcp2-white-dwarf-armadillos/blob/master/Screen%20Shot%202018-11-15%20at%2010.18.16%20AM.png)

Resources
---------
Coding standards and the grading rubric are posted on D2L.

Data from [Joyce et al. (2018), MNRAS, 479, 1612 (Table 4)](https://doi.org/10.1093/mnras/sty1425)
