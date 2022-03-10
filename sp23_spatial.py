import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, ConvexHull, KDTree
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming


def triangulation():
    points = np.array([
        [2, 4], [3, 4],
        [3, 0], [2, 2],
        [4, 1]
    ])

    simplices = Delaunay(points).simplices
    plt.triplot(points[:, 0], points[:, 1], simplices)
    plt.scatter(points[:, 0], points[:, 1], color='r')
    plt.title('triangulation')
    plt.show()


def convex_hull():
    points = np.array([
        [2, 4], [3, 4],
        [3, 0], [2, 2],
        [4, 1], [1, 2],
        [5, 0], [3, 1],
        [1, 2], [0, 2]
    ])

    hull = ConvexHull(points)
    hull_points = hull.simplices

    plt.scatter(points[:, 0], points[:, 1])
    for simplex in hull_points:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    plt.title('convex_hull')
    plt.show()


def kdtree():
    points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
    kdtree = KDTree(points)
    res = kdtree.query((1, 1))
    print('kdtree', res)


def euclidean_distance():
    p1 = (1, 0)
    p2 = (10, 2)
    res = euclidean(p1, p2)
    print('euclidean_distance', res)


def cityblock_distance():
    p1 = (1, 0)
    p2 = (10, 2)
    res = cityblock(p1, p2)
    print('city_block', res)


def cosine_distance():
    p1 = (1, 0)
    p2 = (10, 2)
    res = cosine(p1, p2)
    print('co_sine', res)


def hamming_distance():
    p1 = (True, False, True)
    p2 = (False, True, True)
    res = hamming(p1, p2)
    print('hamming', res)


triangulation()
convex_hull()
kdtree()
euclidean_distance()
cityblock_distance()
cosine_distance()
hamming_distance()

# https://www.w3schools.com/python/scipy_spatial_data.asp