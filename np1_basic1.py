import numpy as np


def fst():
    arr = np.array([[1, 2, 3], [4, 2, 5]])  # Creating array object
    print("Array is of type: ", type(arr))  # Printing type of arr object
    print("No. of dimensions: ", arr.ndim)  # Printing array dimensions (axes)
    print("Shape of array: ", arr.shape)  # Printing shape of array
    print("Size of array: ", arr.size)  # Printing size (total number of elements) of array
    print("Array stores elements of type: ", arr.dtype)  # Printing type of elements in array


def sec():
    b = np.array((1, 3, 2))  # Creating array from tuple
    print("Array created using passed tuple:", b)

    c = np.zeros((3, 4))  # Creating a 3X4 array with all zeros
    print("An array initialized with all zeros:", c)

    d = np.full((3, 3), 6, dtype='complex')  # Create a constant value array of complex type
    print("An array initialized with all 6s. Array type is complex:", d)

    e = np.random.random((2, 2))  # Create an array with random values
    print("A random array:", e)

    f = np.arange(0, 30, 5)  # Create a sequence of integers from 0 to 30 with steps of 5
    print("A sequential array with steps of 5:", f)

    g = np.linspace(0, 5, 10)  # Create a sequence of 10 values in range 0 to 5
    print("A sequential array with 10 values between 0 and 5:", g)

    arr = np.array([[1, 2, 3, 4],  # Reshaping 3X4 array to 2X2X3 array
                    [5, 2, 4, 2],
                    [1, 2, 0, 1]])

    newarr = arr.reshape(2, 2, 3)
    print("Original array:", arr)
    print("Reshaped array:", newarr)

    arr = np.array([[1, 2, 3], [4, 5, 6]])  # Flatten array
    flarr = arr.flatten()

    print("Original array:", arr)
    print("Fattened array:", flarr)


def thrd():
    arr = np.array([[-1, 2, 0, 4],
                    [4, -0.5, 6, 0],
                    [2.6, 0, 7, 8],
                    [3, -7, 4, 2.0]])

    temp = arr[:2, 0:4:2]  # Slicing array
    print("Array with first 2 rows and alternate columns(0 and 2):", temp)

    temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]  # Integer array indexing example
    print("Elements at indices (0, 3), (1, 2), (2, 1), (3, 0):", temp)

    # boolean array indexing example
    cond = arr > 0  # cond is a boolean array
    temp = arr[cond]
    print("Elements greater than 0:", temp)


def frth():
    a = np.array([1, 2, 5, 3])

    print("Adding 1 to every element:", a + 1)  # add 1 to every element
    print("Subtracting 3 from each element:", a - 3)  # subtract 3 from each element
    print("Multiplying each element by 10:", a * 10)  # multiply each element by 10
    print("Squaring each element:", a ** 2)  # square each element

    a *= 2  # modify existing array
    print("Doubled each element of original array:", a)

    a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])  # transpose of array
    print("Original array:", a)
    print("Transpose of array:", a.T)


def fifth():
    arr = np.array([[1, 5, 6],
                    [4, 7, 2],
                    [3, 1, 9]])

    print("Largest element is:", arr.max())  # maximum element of array
    print("Row-wise maximum elements:", arr.max(axis=1))
    print("Column-wise minimum elements:", arr.min(axis=0))  # minimum element of array
    print("Sum of all array elements:", arr.sum())  # sum of array elements
    print("Cumulative sum along each row:", arr.cumsum(axis=1))  # cumulative sum along each row


def sixth():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[4, 3], [2, 1]])

    print("Array sum:", a + b)  # add arrays
    print("Array multiplication:", a * b)  # multiply arrays (element wise multiplication)
    print("Matrix multiplication:", a.dot(b))  # matrix multiplication


def svnth():
    a = np.array([0, np.pi / 2, np.pi])  # create an array of sine values
    print("Sine values of array elements:", np.sin(a))

    b = np.array([0, 1, 2, 3])  # exponential values
    print("Exponent of array elements:", np.exp(b))

    print("Square root of array elements:", np.sqrt(b))  # square root of array values


def egth():
    a = np.array([[1, 4, 2],
                  [3, 4, 6],
                  [0, -1, 5]])

    print("Array elements in sorted order:", np.sort(a, axis=None))  # sorted array
    print("Row-wise sorted array:", np.sort(a, axis=1))  # sort array row-wise
    print("Column wise sort by applying merge-sort:", np.sort(a, axis=0, kind='mergesort'))  # specify sort algorithm

    dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]  # Example to show sorting of structured array. set alias names for dtypes
    values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]  # Values to be put in array

    arr = np.array(values, dtype=dtypes)  # Creating array
    print("Array sorted by names:", np.sort(arr, order='name'))
    print("Array sorted by graduation year and then cgpa:", np.sort(arr, order=['grad_year', 'cgpa']))


if __name__ == '__main__':
    fst()
    sec()
    thrd()
    frth()
    fifth()
    sixth()
    svnth()
    egth()

# https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/