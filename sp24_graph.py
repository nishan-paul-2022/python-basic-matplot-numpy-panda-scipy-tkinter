import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order


def connected_components_graph():  # Find all of the connected components
    arr = np.array([
        [0, 1, 2],
        [1, 0, 0],
        [2, 0, 0]
    ])
    newarr = csr_matrix(arr)
    print('graphs', connected_components(newarr))


def dijkstra_graph():
    arr = np.array([
        [0, 1, 2],
        [1, 0, 0],
        [2, 0, 0]
    ])
    newarr = csr_matrix(arr)
    print(dijkstra(newarr, return_predecessors=True, indices=0))


def floyd_warshall_graph():
    arr = np.array([
        [0, 1, 2],
        [1, 0, 0],
        [2, 0, 0]
    ])
    newarr = csr_matrix(arr)
    print(floyd_warshall(newarr, return_predecessors=True))


def bellman_ford_graph():
    arr = np.array([
        [0, -1, 2],
        [1, 0, 0],
        [2, 0, 0]
    ])
    newarr = csr_matrix(arr)
    print(bellman_ford(newarr, return_predecessors=True, indices=0))


def depth_first_order_graph():
    arr = np.array([
        [0, 1, 0, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 0],
        [0, 1, 0, 1]
    ])
    newarr = csr_matrix(arr)
    print(depth_first_order(newarr, 1))


def breadth_first_order_graph():
    arr = np.array([
        [0, 1, 0, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 0],
        [0, 1, 0, 1]
    ])
    newarr = csr_matrix(arr)
    print(breadth_first_order(newarr, 1))


connected_components_graph()
dijkstra_graph()
floyd_warshall_graph()
bellman_ford_graph()
depth_first_order_graph()
breadth_first_order_graph()

# https://www.w3schools.com/python/scipy_graphs.asp