"""
===================
Detrending a signal
===================

:func:`scipy.signal.detrend` removes a linear trend.
"""

# Generate a random signal with a trend
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


t = np.linspace(0, 5, 100)
x = t + np.random.normal(size=100)

# Detrend
x_detrended = signal.detrend(x)

# Plot
plt.figure(figsize=(5, 4))
plt.plot(t, x, label="x")
plt.plot(t, x_detrended, label="x_detrended")
plt.legend(loc='best')
plt.show()
