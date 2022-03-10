import numpy as np


def fst():
    bat = np.array([
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]]
    ])
    batans = bat[..., 1]  # Equivalent to b[:, :, 1]
    print(batans)

    cat = np.arange(10, 1, -2)
    catans = cat[[3, 1, 2]]  # Indexes are specified inside array
    print(catans)

    rat = np.array([[1, 2], [3, 4], [5, 6]])
    ratans = rat[[0, 1, 2], [0, 0, 1]]
    print(ratans)


def sec():
    a = np.array([10, 40, 80, 50, 100])
    print(a[a > 50])
    print(a[a % 40 == 0] ** 2)

    b = np.array([[[5, 5], [4, 5], [16, 4]], [[7, 23], [1, 6], [14, 16]]])
    sumrow = b.sum(-1)
    print(sumrow)
    print(b[sumrow % 10 == 0])


def thrd():
    array = np.arange(12).reshape(3, 4)
    print("Original array : ", array)

    a = np.compress([1, 0], array, axis=0)
    print("Sliced array : ", a)

    b = np.compress([False, True], array, axis=0)
    print("Sliced array : ", b)


def frth():
    array2D = np.array([[93, 95],
                        [84, 100],
                        [99, 87]])

    print("positive indexing: ", array2D[1, 0])
    print("negative indexing: ", array2D[-2, 0])

    print("slicing using positive indices: ", array2D[1:3, 1])
    print("slicing using positive indices: ", array2D[:, 1])
    print("slicing using negative indices: ", array2D[:, -1])


def fifth():
    arr = np.array([[1, 20, 3, 1],
                    [40, 5, 66, 7],
                    [70, 88, 9, 11],
                    [80, 100, 50, 77],
                    [1, 8.5, 7.9, 4.8]])
    print(arr)
    print("arr[:, 1]: ", arr[:, 1])
    print("arr[:, [1]]: ", arr[:, [1]])
    print("arr[[0, 1]]:", arr[[0, 1]])
    print("arr[0, 1]", arr[0, 1])


def sixth():
    a = np.tril_indices(3)
    print(a)
    b = np.tril_indices(3, 2)
    print(b)


if __name__ == '__main__':
    # fst()
    # sec()
    # thrd()
    # frth()
    # fifth()
    sixth()

# https://www.npsfornps.org/indexing-in-numpy/
# https://www.geeksforgeeks.org/numpy-compress-python/
# https://www.geeksforgeeks.org/how-to-access-different-rows-of-a-multidimensional-numpy-array/
# https://www.geeksforgeeks.org/numpy-tril_indices-function-python/