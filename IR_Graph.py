# Physics 216
# Plotting code to use the whole year!
# Jaylene Naylor
# September 2015, modified Sept 2017, August 2018
# -------------------------------------------#
# Import packages and libraries needed and give them shortcut names
#from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------#
# Data Section - Create Arrays for data. Perform necessary calculations
# CHANGE THE VARIABLE NAMES and numbers to match your data
Current = np.array([0.0039, 0.0061, 0.012, 0.0245, 0.037, 0.0462, 0.0585, 0.0695, 0.0812, 0.0934, 0.1045, 0.115])  # what are units?
Voltage = np.array([0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])  # what are units?

# --------------------------------------------#
# Create arrays for uncertainties
# CHANGE THE VARIABLE NAME and numbers to match your data
err_Voltage = np.array([0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001])

# --------------------------------------------#
# Re-assign variables as x, y, dy so that the following code may remain generic

x = Current  # this should be the array you want to plot on the x axis
y = Voltage
dy = err_Voltage  # this should be your error in y array

# ----------------------------------------------#
# Don't need to change anything in this section!

# Find the intercept and slope, b and m, from Python's polynomial fitting function
b, m = np.polynomial.polynomial.polyfit(x, y, 1, w=dy)

# Write the equation for the best fit line based on the slope and intercept
fit = b + m * x


# Calculate the error in slope and intercept
# def Delta(x, dy) is a function, and we will learn how to write our own at a later date. They are very useful!
def Delta(x, dy):
    D = (sum(1 / dy ** 2)) * (sum(x ** 2 / dy ** 2)) - (sum(x / dy ** 2)) ** 2
    return D


D = Delta(x, dy)

dm = np.sqrt(1 / D * sum(1 / dy ** 2))  # error in slope
db = np.sqrt(1 / D * sum(x ** 2 / dy ** 2))  # error in intercept


# Calculate the "goodness of fit" from the linear least squares fitting document
def LLSFD2(x, y, dy):
    N = sum(((y - b - m * x) / dy) ** 2)
    return N


N = LLSFD2(x, y, dy)

# -----------------------------------------------------------------------#
# Plot data on graph. Plot error bars and place values for slope, error in slope and goodness of fit on the plot using "annotate"
plt.figure(figsize=(15, 10))

plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')

# create labels  YOU NEED TO CHANGE THESE!!!
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.title('Current vs. Voltage')

plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none")  # don't need to plot x error bars

plt.annotate('Slope (Ohms) = {value:.{digits}E}'.format(value=m, digits=2),
             (0.05, 0.9), xycoords='axes fraction')

plt.annotate('Error in Slope (Ohms) = {value:.{digits}E}'.format(value=dm, digits=1),
             (0.05, 0.85), xycoords='axes fraction')

plt.annotate('Goodness of fit = {value:.{digits}E}'.format(value=N, digits=2),
             (0.05, 0.80), xycoords='axes fraction')

plt.show()