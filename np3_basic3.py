import numpy as np


def fst():
    x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))  # Initializing value of x-axis and y-axis in the range -1 to 1
    dst = np.sqrt(x*x+y*y)
    sigma = 1  # Initializing sigma and muu
    muu = 0.000
    gauss = np.exp(-((dst-muu)**2 / (2.0 * sigma**2)))  # Calculating Gaussian array
    print("2D Gaussian array: ", gauss)


def sec():
    list1 = [5, 6, 9]  # creating a 1-D list (Horizontal)
    list2 = [1, 2, 3]  # creating a 1-D list (Horizontal)

    vector1 = np.array(list1)  # creating first vector
    print("First Vector: " + str(vector1))  # printing vector1

    vector2 = np.array(list2)  # creating second vector
    print("Second Vector: " + str(vector2))  # printing vector2

    addition = vector1 + vector2  # adding both the vector | a + b = (a1 + b1, a2 + b2, a3 + b3)
    print("Vector Addition: " + str(addition))  # printing addition vector

    subtraction = vector1 - vector2  # subtracting both the vector | a - b = (a1 - b1, a2 - b2, a3 - b3)
    print("Vector Subtraction : " + str(subtraction))  # printing addition vector

    multiplication = vector1 * vector2  # multiplying both the vector | a * b = (a1 * b1, a2 * b2, a3 * b3)
    print("Vector Multiplication : " + str(multiplication))  # printing multiplication vector

    division = vector1 / vector2  # dividing both the vector | a / b = (a1 / b1, a2 / b2, a3 / b3)
    print("Vector Division: " + str(division))  # printing division vector


def thrd():
    list1, list2 = [5, 6, 9], [1, 2, 3]
    vector1, vector2 = np.array(list1), np.array(list2)
    dot_product = vector1.dot(vector2)   # getting dot product of both the vectors | a . b = (a1b1 + a2b2 + a3b3)
    print("Dot Product : " + str(dot_product))  # printing dot product


def frth():
    list1 = [1, 2, 3]
    vector = np.array(list1)
    scalar = 2  # scalar value
    scalar_mul = vector * scalar  # getting scalar multiplication value | s * v = (s * v1, s * v2, s * v3)
    print("Scalar Multiplication: " + str(scalar_mul))  # printing dot product


def fifth():
    gfg = np.core.records.fromrecords([(101, 'Jitender', 21), (102, 'Deepak', 20)], names='roll, name, age')
    print(gfg[0])
    print(gfg.name)


if __name__ == '__main__':
    fst()
    sec()
    thrd()
    frth()
    fifth()

# https://www.geeksforgeeks.org/how-to-generate-2-d-gaussian-array-using-numpy/
# https://www.geeksforgeeks.org/how-to-create-a-vector-in-python-using-numpy/
# https://www.geeksforgeeks.org/python-numpy-fromrecords-method/