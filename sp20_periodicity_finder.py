"""
==========================
Crude periodicity finding
==========================

Discover the periods in evolution of animal populations
(:download:`E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/populations.txt`)
"""
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

data = np.loadtxt('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/sp20_populations.txt')
years = data[:, 0]
populations = data[:, 1:]

# Plot the data

plt.figure()
plt.plot(years, populations * 1e-3)
plt.xlabel('Year')
plt.ylabel('Population number ($\cdot10^3$)')
plt.legend(['hare', 'lynx', 'carrot'], loc=1)

# Plot its periods

ft_populations = fftpack.fft(populations, axis=0)
frequencies = fftpack.fftfreq(populations.shape[0], years[1] - years[0])
periods = 1 / frequencies

plt.figure()
plt.plot(periods, abs(ft_populations) * 1e-3, 'o')
plt.xlim(0, 22)
plt.xlabel('Period')
plt.ylabel('Power ($\cdot10^3$)')

plt.show()

# There's probably a period of around 10 years (obvious from the plot),
# but for this crude a method, there's not enough data to say much more.
