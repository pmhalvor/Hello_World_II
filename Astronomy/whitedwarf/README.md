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

1. Use the `wiki` for this repository to write a report of your findings. Make sure you address the questions in the instructions in your report.
2. Modify this README file by replacing instructions from me with your  instructions on how to run the code.
3. Post a message on your team's Slack channel `@Dylan Mankel` and `@Edward Brown` or DM us when you are ready to have your code reviewed.

Resources
---------
Coding standards and the grading rubric are posted on D2L.

Data from [Joyce et al. (2018), MNRAS, 479, 1612 (Table 4)](https://doi.org/10.1093/mnras/sty1425)
