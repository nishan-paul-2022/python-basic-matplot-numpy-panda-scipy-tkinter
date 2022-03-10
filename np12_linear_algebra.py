import numpy as np
import math
import matplotlib.pyplot as plt


def fst():
    A = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    print("Rank of A:", np.linalg.matrix_rank(A))  # Rank of a matrix
    print("Trace of A:", np.trace(A))  # Trace of matrix A
    print("Determinant of A:", np.linalg.det(A))  # Determinant of a matrix
    print("Inverse of A: ", np.linalg.inv(A))  # Inverse of matrix A
    print("Matrix A raised to power 3: ", np.linalg.matrix_power(A, 3))


def sec(a):
    arr = np.array(a)
    print("Printing the Original square array: ", arr)

    w, v = np.linalg.eig(arr)  # finding eigenvalues and eigenvectors
    print("Printing the Eigen values of the given square array: ", w)  # printing eigen values
    print("Printing Right eigenvectors of the given square array: ", v)  # printing eigen vectors


def thrd():
    vector_a = 2 + 3j
    vector_b = 4 + 5j
    product = np.vdot(vector_a, vector_b)
    print("Dot Product  : ", product)


def frth():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([8, 18])
    print("Solution of linear equations:", np.linalg.solve(a, b))

    x = np.arange(0, 9)  # x co-ordinates
    A = np.array([x, np.ones(9)])

    y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]  # linearly generated sequence
    w = np.linalg.lstsq(A.T, y)[0]  # obtaining the parameters of regression line

    line = w[0] * x + w[1]  # plotting the regression line
    plt.plot(x, line, 'r-')
    plt.plot(x, y, 'o')
    plt.show()


def fifth(a):
    arr = np.array(a)
    q, r = np.linalg.qr(arr)  # Find the QR factor of array
    print("Decomposition of matrix: {} {}".format(q, r))


def sixth():
    v = np.array([0, 1, 2, 3, 4])
    magnitude = math.sqrt(sum(pow(element, 2) for element in v))
    print('Magnitude of the Vector:', magnitude)


if __name__ == '__main__':
    fst()
    sec([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
    sec([[1, -2j], [2j, 5]])
    thrd()
    frth()
    fifth([[10, 22], [13, 6]])
    fifth([[0, 1], [1, 0], [1, 1], [2, 2]])
    sixth()

# https://www.geeksforgeeks.org/numpy-linear-algebra/
# https://www.geeksforgeeks.org/get-the-qr-factorization-of-a-given-numpy-array/
# https://www.geeksforgeeks.org/how-to-get-the-magnitude-of-a-vector-in-numpy/
# https://www.geeksforgeeks.org/how-to-compute-the-eigenvalues-and-right-eigenvectors-of-a-given-square-array-using-numpy/