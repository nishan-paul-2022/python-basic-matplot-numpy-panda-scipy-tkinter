import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from matplotlib.ticker import LinearLocator


def interpolating_1():
    A = np.random.rand(5, 5)

    fig, axs = plt.subplots(1, 3, figsize=(10, 3))
    for ax, interp in zip(axs, ['nearest', 'bilinear', 'bicubic']):
        ax.imshow(A, interpolation=interp)
        ax.set_title(interp.capitalize())
        ax.grid(True)

    plt.show()


def interpolating_2():
    x = np.arange(120).reshape((10, 12))

    fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
    interp = 'bilinear'

    axs[0].set_title('blue should be up')
    axs[0].imshow(x, origin='upper', interpolation=interp)

    axs[1].set_title('blue should be down')
    axs[1].imshow(x, origin='lower', interpolation=interp)
    plt.show()


def interpolating_3():
    delta = 0.025
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X ** 2 - Y ** 2)
    Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
    Z = (Z1 - Z2) * 2

    path = Path([[0, 1], [1, 0], [0, -1], [-1, 0], [0, 1]])
    patch = PathPatch(path, facecolor='none')

    fig, ax = plt.subplots()
    ax.add_patch(patch)

    im = ax.imshow(Z, interpolation='bilinear', cmap=cm.gray, origin='lower', extent=[-3, 3, -3, 3], clip_path=patch, clip_on=True)
    im.set_clip_path(patch)
    plt.show()


def histogram():
    # example data
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    x = mu + sigma * np.random.randn(437)
    num_bins = 437

    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(x, num_bins, density=True)  # the histogram of the data

    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))  # add a 'best fit' line

    ax.plot(bins, y, '--')
    ax.set_xlabel('Smarts')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

    fig.tight_layout()  # Tweak spacing to prevent clipping of ylabel
    plt.show()


def path_patch_object():
    fig, ax = plt.subplots()

    Path = mpath.Path
    path_data = [
        (Path.MOVETO, (1.58, -2.57)),
        (Path.CURVE4, (0.35, -1.1)),
        (Path.CURVE4, (-1.75, 2.0)),
        (Path.CURVE4, (0.375, 2.0)),
        (Path.LINETO, (0.85, 1.15)),
        (Path.CURVE4, (2.2, 3.2)),
        (Path.CURVE4, (3, 0.05)),
        (Path.CURVE4, (2.0, -0.5)),
        (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
    ax.add_patch(patch)

    # plot control points and connecting lines
    x, y = zip(*path.vertices)
    ax.plot(x, y, 'go-')

    ax.grid()
    ax.axis('equal')
    plt.show()


def surface_color_map_3d():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # Make data.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)  # Plot the surface.

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter('{x:.02f}')  # A StrMethodFormatter is used automatically
    fig.colorbar(surf, shrink=0.5, aspect=5)  # Add a color bar which maps values to colors.
    plt.show()


if __name__ == '__main__':
    interpolating_1()
    interpolating_2()
    interpolating_3()
    histogram()
    path_patch_object()
    surface_color_map_3d()


# https://matplotlib.org/stable/gallery/statistics/histogram_features.html
# https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html
# https://matplotlib.org/stable/gallery/mplot3d/surface3d.html