# Normal distribution: histogram and PDF
# Explore the normal distribution: a histogram built from samples and the
# PDF (probability density function).

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt


# Sample from a normal distribution using numpy's random number generator
samples = np.random.normal(size=10000)

# Compute a histogram of the sample
bins = np.linspace(-5, 5, 30)
histogram, bins = np.histogram(samples, bins=bins, density=True)

bin_centers = 0.5*(bins[1:] + bins[:-1])

# Compute the PDF on the bin centers from scipy distribution object
pdf = stats.norm.pdf(bin_centers)

plt.figure(figsize=(6, 4))
plt.plot(bin_centers, histogram, label="Histogram of samples")
plt.plot(bin_centers, pdf, label="PDF")
plt.legend()
plt.show()