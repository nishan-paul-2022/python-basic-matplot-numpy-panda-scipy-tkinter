import numpy as np


def fst():
    array_1 = np.array([1, 2])
    array_2 = np.array([3, 4])
    array_new = np.concatenate((array_1, array_2))
    print(array_new)


def sec():
    block_1 = np.array([[1, 1], [1, 1]])
    block_2 = np.array([[2, 2, 2], [2, 2, 2]])
    block_3 = np.array([[3, 3], [3, 3], [3, 3]])
    block_4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
    block_new = np.block([[block_1, block_2], [block_3, block_4]])
    print(block_new)


def thrd():
    gfg1 = np.array([1, 2, 3])
    gfg2 = np.array([4, 5, 6])
    result1 = np.ma.concatenate([gfg1, gfg2])
    print(result1)

    result2 = np.ma.concatenate([[gfg1], [gfg2]])
    print(result2)


def frth():
    gfg1 = np.array([1, 2, 3])
    gfg2 = np.array([4, 5, 6])
    result1 = np.dstack((gfg1, gfg2))
    print(result1)  # using numpy.dstack() method

    gfg3 = np.array([[10], [2], [13]])
    gfg4 = np.array([[41], [55], [6]])
    result2 = np.dstack((gfg3, gfg4))
    print(result2)  # using numpy.dstack() method


def fifth():  # Horizontal splitting
    a = np.arange(9).reshape(3, 3)  # Making of a 3x3 array
    asplit = np.hsplit(a, 3)  # Horizontal splitting of array 'a' using np.hsplit()
    asplit1 = np.split(a, 3, 1)  # Horizontal splitting of array 'a' using 'split' with axis parameter = 1

    print("The array {} gets splitted horizontally to form {} ".format(a, asplit))
    print("The array {} gets splitted horizontally to form {} ".format(a, asplit1))


def sixth():  # Vertical splitting
    a = np.arange(9).reshape(3, 3)  # Making of a 3x3 array
    asplit = np.vsplit(a, 3)  # Vertical splitting of array 'a' using np.vsplit()
    asplit1 = np.split(a, 3, 0)  # Vertical splitting of array 'a' using 'split' with axis parameter = 0

    print("The array {} gets splitted vertically to form {} ".format(a, asplit))
    print("The array {} gets splitted vertically to form {} ".format(a, asplit1))


def seventh():  # Depth-wise splitting
    b = np.arange(27).reshape(3, 3, 3)  # Making of a 3x3x3 array.
    bsplit = np.dsplit(b, 3)  # Depth-wise splitting of array 'b' using np.dsplit()
    print("The array {} gets splitted depth-wise to form {}".format(b, bsplit))


def eight():
    an_array = np.array([[1, 2], [3, 4]])
    another_array = np.array([[1, 2], [3, 4]])
    comparison = an_array == another_array
    equal_arrays = comparison.all()
    print(equal_arrays)

    a = np.array([101, 99, 87])
    b = np.array([897, 97, 111])
    print("a > b: ", np.greater(a, b))
    print("a >= b: ", np.greater_equal(a, b))
    print("a < b: ", np.less(a, b))
    print("a <= b: ", np.less_equal(a, b))


if __name__ == '__main__':
    fst()
    sec()
    thrd()
    frth()
    fifth()
    sixth()
    seventh()
    eight()

# https://www.geeksforgeeks.org/joining-numpy-array/
# https://www.geeksforgeeks.org/python-numpy-np-ma-concatenate-method/
# https://www.geeksforgeeks.org/python-numpy-dstack-method/
# https://www.geeksforgeeks.org/splitting-arrays-in-numpy/
# https://www.geeksforgeeks.org/how-to-compare-two-numpy-arrays/
# https://www.geeksforgeeks.org/find-the-union-of-two-numpy-arrays/