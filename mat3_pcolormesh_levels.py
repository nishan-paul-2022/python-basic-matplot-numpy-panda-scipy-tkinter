import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np


def basic_pcolormesh():
    Z = np.random.rand(6, 10)
    x = np.arange(-0.5, 10, 1)  # len = 11
    y = np.arange(4.5, 11, 1)  # len = 7

    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, Z)
    plt.show()


def non_rectilinear_pcolormesh():
    Z = np.random.rand(6, 10)
    x = np.arange(-0.5, 10, 1)  # len = 11
    y = np.arange(4.5, 11, 1)  # len = 7
    X, Y = np.meshgrid(x, y)
    X = X + 0.2 * Y  # tilt the coordinates.
    Y = Y + 0.3 * X

    fig, ax = plt.subplots()
    ax.pcolormesh(X, Y, Z)
    plt.show()


def centered_coordinates():
    Z = np.random.rand(6, 10)
    x = np.arange(10)  # len = 10
    y = np.arange(6)  # len = 6
    X, Y = np.meshgrid(x, y)

    fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)

    axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
    axs[0].set_title("shading='auto'='nearest'")

    axs[1].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='flat')
    axs[1].set_title("shading='flat'")

    plt.show()


def making_levels_using_norms():
    dx, dy = 0.05, 0.05  # make these smaller to increase the resolution
    y, x = np.mgrid[slice(1, 5 + dy, dy), slice(1, 5 + dx, dx)]  # generate 2 2d grids for the x & y bounds
    z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)
    z = z[:-1, :-1]
    levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())
    cmap = plt.get_cmap('PiYG')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    fig, (ax0, ax1) = plt.subplots(nrows=2)
    im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    fig.colorbar(im, ax=ax0)
    ax0.set_title('pcolormesh with levels')

    cf = ax1.contourf(x[:-1, :-1] + dx/2., y[:-1, :-1] + dy/2., z, levels=levels, cmap=cmap)
    fig.colorbar(cf, ax=ax1)
    ax1.set_title('contourf with levels')

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    basic_pcolormesh()
    non_rectilinear_pcolormesh()
    centered_coordinates()
    making_levels_using_norms()

# https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html