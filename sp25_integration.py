import scipy.integrate
from numpy import exp
from math import sqrt
import numpy as np


def single():
    f = lambda x: exp(-x ** 2)
    i = scipy.integrate.quad(f, 0, 1)
    print(i)


def double():
    f = lambda x, y: 16 * x * y
    g = lambda x: 0
    h = lambda y: sqrt(1 - 4 * y ** 2)
    i = scipy.integrate.dblquad(f, 0, 0.5, g, h)
    print(i)


def triple():
    f = lambda z, y, x: y * np.sin(x) + z * np.cos(x)
    g, h = lambda x: 0, lambda x: 1  # y limits
    i, j = lambda x, y: -1, lambda x, y: 1  # z limits
    ans, err = scipy.integrate.tplquad(f, 0, np.pi, g, h, i, j)
    print(ans)


single()
double()
triple()