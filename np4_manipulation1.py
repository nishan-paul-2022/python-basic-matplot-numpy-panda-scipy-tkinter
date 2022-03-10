import numpy as np


def fst():
    ary = np.array([13, 99, 100, 34, 65, 11, 66, 81, 632, 44])
    copy = np.empty_like(ary)
    copy[:] = ary
    print("Copy of the given array: ", copy)


def sec():
    org_array = np.array([[99, 22, 33], [44, 77, 66]])
    copy_array = org_array
    org_array[1, 2] = 13
    print("Original Array: ", org_array)
    print("Copied Array: ", copy_array)


def thrd():
    org_array = np.array([[23, 46, 85], [43, 56, 99], [11, 34, 55]])
    print("Original array: ", org_array)
    copy_array = np.copy(org_array)
    print("Copied array: ", copy_array)


def frth():
    arr = np.array([1, 8, 3, 3, 5])
    print('Original Array: ', arr)
    arr = np.append(arr, [7])  # appending to the array
    print('Array after appending: ', arr)


def fifth():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.append(arr1, arr2)  # appending arr2 to arr1
    print('Array after appending : ', arr)


def sixth():
    arr = np.arange(1, 13).reshape(2, 6)
    print('Original Array: ', arr)

    col = np.arange(5, 11).reshape(1, 6)  # create another array which is to be appended column-wise
    print('Array to be appended column wise: ', col)
    arr_col = np.append(arr, col, axis=0)
    print('Array after appending the values column wise: ', arr_col)

    row = np.array([1, 2]).reshape(2, 1)  # create an array which is to be appended row wise
    print('Array to be appended row wise: ', row)
    arr_row = np.append(arr, row, axis=1)
    print('Array after appending the values row wise: ', arr_row)


def sevnth():
    my_array = np.arange(12).reshape(4, 3)
    print("Original array: ", my_array)

    my_array[:, [2, 0]] = my_array[:, [0, 2]]  # swapping the column with index of original array
    print("After swapping arrays the last column and first column: ", my_array)


def egth():
    x = np.random.random((3, 4))
    x3D = np.expand_dims(x, axis=2)
    print(x)
    print(x3D)
    print(x3D.shape)

    y = np.arange(5 * 5).reshape(5, 5)
    newaxes = (0, 3, -1)
    y5D = np.expand_dims(y, axis=newaxes)
    print(y)
    print(y5D)


def nine():
    in_arr1 = np.array([1, 2, 3])
    in_arr2 = np.array([4, 5, 6])
    out_arr = np.hstack((in_arr1, in_arr2))  # Stacking the two arrays horizontally
    print("Output horizontally stacked array: ", out_arr)

    in_arr1 = np.array([[1, 2, 3], [-1, -2, -3]])
    in_arr2 = np.array([[4, 5, 6], [-4, -5, -6]])
    out_arr = np.hstack((in_arr1, in_arr2))  # Stacking the two arrays horizontally
    print("Output stacked array: ", out_arr)


def ten():
    in_arr1 = np.array([1, 2, 3])
    in_arr2 = np.array([4, 5, 6])
    out_arr = np.vstack((in_arr1, in_arr2))  # Stacking the two arrays vertically
    print("Output vertically stacked array: ", out_arr)

    in_arr1 = np.array([[1, 2, 3], [-1, -2, -3]])
    in_arr2 = np.array([[4, 5, 6], [-4, -5, -6]])
    out_arr = np.vstack((in_arr1, in_arr2))   # Stacking the two arrays vertically
    print("Output stacked array : ", out_arr)


def eleven(n=8):  # Python program to print nXn Assuming that n is always even as a checkerboard was
    print("Checkerboard pattern:")
    x = np.zeros((n, n), dtype=int)  # create a n * n matrix

    x[1::2, ::2] = 1  # fill with 1 the alternate rows and columns
    x[::2, 1::2] = 1

    for i in range(n):  # print the pattern
        for j in range(n):
            print(x[i][j], end=" ")
        print()


if __name__ == '__main__':
    fst()
    sec()
    thrd()
    frth()
    fifth()
    sixth()
    sevnth()
    egth()
    nine()
    ten()
    eleven()

# https://www.npsfornps.org/how-to-copy-numpy-array-into-another-array/
# https://www.npsfornps.org/appending-values-at-the-end-of-an-numpy-array/
# https://www.npsfornps.org/appending-values-at-the-end-of-an-numpy-array/
# https://www.npsfornps.org/how-to-swap-columns-of-a-given-numpy-array/
# https://www.npsfornps.org/insert-a-new-axis-within-a-numpy-array/
# https://www.npsfornps.org/numpy-hstack-in-python/
# https://www.geeksforgeeks.org/numpy-vstack-in-python/
# https://www.geeksforgeeks.org/python-program-print-checkerboard-pattern-nxn-using-numpy/
