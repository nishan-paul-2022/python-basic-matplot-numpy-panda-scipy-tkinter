# Curve fitting: temperature as a function of month of the year
# We have the min and max temperatures in Alaska for each months of the year.
# We would like to find a function to describe this yearly evolution. For this, we will fit a periodic function.
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def yearly_temps(times, avg, ampl, time_offset):  # Fitting it to a periodic function
    return avg + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max())


temp_max = np.array([17,  19,  21,  28,  33,  38, 37,  37,  31,  23,  19,  18])
temp_min = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])

months = np.arange(12)
plt.plot(months, temp_max, 'ro')
plt.plot(months, temp_min, 'bo')
plt.xlabel('Month')
plt.ylabel('Min and max temperature')

res_max, cov_max = optimize.curve_fit(yearly_temps, months, temp_max, [20, 10, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months, temp_min, [-40, 20, 0])

days = np.linspace(0, 12, num=365)  # Plotting the fit
plt.figure()
plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')
plt.show()