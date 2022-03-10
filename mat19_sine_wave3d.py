import numpy as np
import matplotlib.pyplot as plt


def fst():
    # Creating array points using numpy
    x = np.arange(0, 20, 0.1)
    y = np.sin(x)
    z = y*np.sin(x)
    c = x + y

    fig = plt.figure(figsize=(10, 10))  # Change the Size of Graph using Figsize
    ax = plt.axes(projection='3d')  # Generating a 3D sine wave

    ax.scatter(x, y, z, c=c)  # To create a scatter graph
    plt.show()


def sec():
    fig = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection='3d')

    # Creating array points using numpy
    z = np.linspace(0, 15, 1000)
    x = np.sin(z)
    y = np.cos(z)

    ax.plot3D(x, y, z, 'gray')
    plt.show()


if __name__ == '__main__':
    fst()
    sec()

# https://www.geeksforgeeks.org/3d-sine-wave-using-matplotlib-python/