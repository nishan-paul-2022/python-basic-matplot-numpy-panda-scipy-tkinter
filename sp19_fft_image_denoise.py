import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack, ndimage


# Show the results
def plot_spectrum(im_fft):
    from matplotlib.colors import LogNorm
    # A logarithmic colormap
    plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5))
    plt.colorbar()


im = plt.imread('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_fruit.png').astype(float)

plt.figure()
plt.imshow(im, plt.cm.gray)
plt.title('Original image')


im_fft = fftpack.fft2(im)  # Compute the 2d FFT of the input image

plt.figure()
plot_spectrum(im_fft)
plt.title('Fourier transform')

# Filter in FFT
# In the lines following, we'll make a copy of the original spectrum and truncate coefficients.
# Define the fraction of coefficients (in each direction) we keep
keep_fraction = 0.1

im_fft2 = im_fft.copy()  # Call ff a copy of the original transform. Numpy arrays have a copy method for this purpose.
r, c = im_fft2.shape[:2]  # Set r and c to be the number of rows and columns of the array.

im_fft2[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0  # Set to zero all rows with indices between r*keep_fraction and r*(1-keep_fraction):
im_fft2[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0  # Similarly with the columns:

plt.figure()
plot_spectrum(im_fft2)
plt.title('Filtered Spectrum')

# Reconstruct the final image
# Reconstruct the denoised image from the filtered spectrum, keep only the real part for display.
im_new = fftpack.ifft2(im_fft2).real

plt.figure()
plt.imshow(im_new, plt.cm.gray)
plt.title('Reconstructed Image')

# Easier and better: :func:`scipy.ndimage.gaussian_filter`
# Implementing filtering directly with FFTs is tricky and time consuming.
# We can use the Gaussian filter from :mod:`scipy.ndimage`
im_blur = ndimage.gaussian_filter(im, 4)

plt.figure()
plt.imshow(im_blur, plt.cm.gray)
plt.title('Blurred image')

plt.show()

# Image denoising by FFT
# Denoise an image by
# implementing a blur with an FFT.
# Implements, via FFT, the following convolution:
# .. math::
#     f_1(t) = \int dt'\, K(t-t') f_0(t')
# .. math::
#     \tilde{f}_1(\omega) = \tilde{K}(\omega) \tilde{f}_0(\omega)