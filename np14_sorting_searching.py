import numpy as np


def fst():
    arr = np.array([10, 32, 30, 50, 20, 82, 91, 45])  # creating the array
    i = np.where(arr == 30)  # looking for value 30 in arr and storing its index in i
    print("arr = {}".format(arr))
    print("i = {}".format(i))


def sec():
    arr = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6]  # creating the array
    left = np.searchsorted(arr, 3, side='left')
    right = np.searchsorted(arr, 3, side='right')
    print("arr = {}".format(arr))
    print("left-most index = {}".format(left))  # left-most 3
    print("right-most index = {}".format(right))  # right-most 3


def thrd():  # returns a sorted copy of an array
    a = np.array([[12, 15], [10, 1]])  # sort along the first axis
    arr1 = np.sort(a, axis=0)
    print("Along first axis: ", arr1)

    a = np.array([[10, 15], [12, 1]])  # sort along the last axis
    arr2 = np.sort(a, axis=-1)
    print("Along last axis: ", arr2)

    a = np.array([[12, 15], [10, 1]])
    arr1 = np.sort(a, axis=None)
    print("Along none axis: ", arr1)


def frth():  # returns the indices that would sort an array
    a = np.array([9, 3, 1, 7, 4, 3, 6])  # Numpy array created
    print('Original array: ', a)  # unsorted array print

    b = np.argsort(a)  # Sort array indices
    print('Sorted indices of original array: ', b)

    c = np.zeros(len(b), dtype=int)  # To get sorted array using sorted indices | c is temp array created of same len as of b
    for i in range(0, len(b)):
        c[i] = a[b[i]]
    print('Sorted array: ', c)


def fifth():  # returns an indirect stable sort using a sequence of keys.
    a = np.array([9, 3, 1, 3, 4, 3, 6])  # First column
    b = np.array([4, 6, 9, 2, 1, 8, 7])  # Second column
    print('column a, column b')
    for (i, j) in zip(a, b):
        print(i, ' ', j)

    ind = np.lexsort((b, a))  # Sort by a then by b
    print('Sorted indices->', ind)


def sixth():  # returns indices of the max element of the array in a particular axis
    array = np.arange(12).reshape(3, 4)  # Working on 2D array
    print("INPUT ARRAY: ", array)
    print("npMax element: ", np.argmax(array))  # No axis mentioned, so works on entire array
    print(("npIndices of Max element: ", np.argmax(array, axis=0)))
    print(("npIndices of Max element: ", np.argmax(array, axis=1)))


def seventh():  # returns indices of the min element of the array in a particular axis
    array = np.arange(12).reshape(3, 4)  # Working on 2D array
    print("INPUT ARRAY: ", array)
    print("npMax element: ", np.argmin(array))  # No axis mentioned, so works on entire array
    print(("npIndices of Max element: ", np.argmin(array, axis=0)))
    print(("npIndices of Max element: ", np.argmin(array, axis=1)))


def eight():  # returns indices of the max element of the array in a particular axis ignoring NaNs.The results cannot be trusted if a slice contains only NaNs and Infs.
    array = np.arange(12).reshape(3, 4)  # Working on 2D array
    print("INPUT ARRAY: ", array)
    print("npMax element: ", np.nanargmax(array))  # No axis mentioned, so works on entire array
    print(("npIndices of Max element: ", np.nanargmax(array, axis=0)))
    print(("npIndices of Max element: ", np.nanargmax(array, axis=1)))


def nine():  # counting a number of non-zero values
    arr = [[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]]
    a = np.count_nonzero(arr)
    print("Number of nonzero values is :", a)


def ten():  # explaining sort_complex() function
    in_arr = [2 + 4j, 5 + 9j, 3 - 2j, 4 - 3j, 3 + 5j, 2 - 4j, 5]
    print("Input array : ", in_arr)
    out_arr = np.sort_complex(in_arr)
    print("Output sorted array : ", out_arr)


def eleven():  # with the help of np.ma.mini() method, we can get the minimum value of masked array
    result = np.ma.array(np.arange(6), mask=[-2, -1, 0, 1, 2, 3]).reshape(3, 2)
    min = result.min()
    print(min)

    result1 = np.ma.array(np.arange(10), mask=[-2, -1, 0, 1, 0, 3, 0, 0, 0, 0]).reshape(2, 5)
    min1 = result1.min()
    print(min1)


if __name__ == '__main__':
    fst()
    # sec()
    # thrd()
    # frth()
    # fifth()
    # sixth()
    # seventh()
    # eight()
    # nine()
    # ten()
    # eleven()

# https://www.npsfornps.org/searching-in-a-numpy-array/
# https://www.npsfornps.org/how-to-sort-a-numpy-array-python/
# https://www.geeksforgeeks.org/numpy-sorting-searching-and-counting/
# https://www.geeksforgeeks.org/numpy-sort_complex-in-python/
# https://www.geeksforgeeks.org/python-numpy-np-ma-mini-method/

