import numpy as np
from functools import reduce


def fst():
    arr1 = np.array([10, 20, 30, 40])
    print("array1 ", arr1)
    arr2 = np.array([20, 40, 60, 80])
    print("array2 ", arr2)
    print("Union of two arrays :", np.union1d(arr1, arr2))  # print union of the two arrays


def sec():  # 2-d array
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    print("array1 ", arr1)
    arr2 = np.array([0, 5, 10])
    print("array2 ", arr2)
    print("Union of two arrays", np.union1d(arr1, arr2))  # print union of 2-d array and 1-d array


def thrd():  # code to find union of more than two arrays
    array = reduce(np.union1d, ([1, 2, 3], [1, 3, 5], [2, 4, 6], [0, 0, 0]))
    print("Union ", array)


def frth():
    arr2D = np.array([[11, 11, 12, 11],  # Create a 2D numpy array
                      [13, 11, 12, 11],
                      [16, 11, 12, 11],
                      [11, 11, 12, 11]])

    print('Original Array: ', arr2D, sep='\n')
    uniqueRows = np.unique(arr2D, axis=0)  # Get unique rows from complete 2D-array by passing axis = 0 in unique function along with 2D-array
    print('Unique Rows: ', uniqueRows, sep='\n')  # print the output result


def fifth():
    a = [1, 2, 2, 4, 3, 6, 4, 8]
    resulta = np.unique(a)  # using np.unique() method
    print(resulta)

    b = [[10.2, 21.4, 3.6, 14.8], [1.0, 5.0, 10.0, 15.0]]
    resultb = np.unique(b)
    print(resultb)


def sixth():
    result = np.array((0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0))
    print(np.trim_zeros(result))
    print(np.trim_zeros(result, 'f'))
    print(np.trim_zeros(result, 'b'))


if __name__ == '__main__':
    fst()
    sec()
    thrd()
    frth()
    fifth()
    sixth()

# https://www.geeksforgeeks.org/find-the-union-of-two-numpy-arrays/
# https://www.geeksforgeeks.org/find-unique-rows-in-a-numpy-array/
# https://www.geeksforgeeks.org/python-numpy-np-unique-method/
# https://www.geeksforgeeks.org/numpy-trim_zeros-in-python/