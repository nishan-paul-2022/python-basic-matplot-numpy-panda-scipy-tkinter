import numpy as np


def determinant(arr):
    n_array = np.array(arr)  # creating a 2X2 Numpy matrix
    print("Numpy Matrix is: ", n_array)  # Displaying the Matrix
    det = np.linalg.det(n_array)  # calculating the determinant of matrix
    print("Determinant of given matrix: ", int(det))


def transpose(arr):
    gfg = np.array(arr)
    geek = gfg.transpose()
    print("Transpose of given matrix: ", geek)


def inverse(arr):
    arr = np.array(arr)
    inverse_array = np.linalg.inv(arr)
    print("Inverse array is: ", inverse_array)


arr = [[50, 29], [30, 44]]

arr1 = [[55, 25, 15],
        [30, 44, 2],
        [11, 45, 77]]

arr2 = [[4, 1, 9],
        [12, 3, 1],
        [4, 5, 6]]

arr4 = [[1, 2], [5, 6]]

arr5 = [[1, 2, 3],
        [4, 9, 6],
        [7, 8, 9]]

determinant(arr)
determinant(arr1)

transpose(arr2)

inverse(arr4)
inverse(arr5)

# https://www.geeksforgeeks.org/how-to-calculate-the-determinant-of-a-matrix-using-numpy/
# https://www.geeksforgeeks.org/python-numpy-matrix-transpose/
# https://www.geeksforgeeks.org/compute-the-inverse-of-a-matrix-using-numpy/