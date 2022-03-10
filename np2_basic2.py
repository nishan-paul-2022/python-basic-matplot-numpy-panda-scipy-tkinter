import numpy as np
from matplotlib import pyplot as plt


def support(x1, y1, data):
    plt.contourf(x1, y1, data, cmap='jet')
    plt.colorbar()
    plt.show()


def fst():
    d = np.ones([5, 2], dtype=float)
    print("Matrix d: ", d)

    b = np.eye(2, dtype=float)  # 2x2 matrix with 1's on main diagonal
    print("Matrix b: np", b)

    a = np.eye(4, 5, k=-1)  # matrix with R=4 C=5 and 1 on diagonal
    print("Matrix a: ", a)


def sec():
    x = np.linspace(-4, 4, 9)  # numpy.linspace creates an array of 9 linearly placed elements between -4 and 4, both inclusive
    y = np.linspace(-5, 5, 11)
    x1, y1 = np.meshgrid(x, y)  # The meshgrid function returns two 2-dimensional arrays

    print('x1: {}\ny1: {}'.format(x1, y1))

    ellipse = x1*2 + 4 * y1**2
    support(x1, y1, ellipse)

    sine = np.sin(x1**2 + y1**2) / (x1**2 + y1**2)
    support(x1, y1, sine)

    random_data = np.random.random((11, 9))
    support(x1, y1, random_data)


if __name__ == '__main__':
    # fst()
    sec()

# https://www.geeksforgeeks.org/numpy-meshgrid-function/