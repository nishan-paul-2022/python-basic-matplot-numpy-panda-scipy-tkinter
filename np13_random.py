import numpy as np
import matplotlib.pyplot as plt


def fst():
    out_arr = np.random.random((3, 3, 2))
    print("Output 3D Array filled with random floats: ", out_arr)

    out_arr = np.random.randint(low=0, high=3, size=5)
    print("Output 1D Array filled with random integers: ", out_arr)

    out_arr = np.random.randint(low=4, size =(2, 3))
    print("Output 2D Array filled with random integers: ", out_arr)


def sec():
    shfl = np.arange(10)
    np.random.shuffle(shfl)
    print(shfl)

    arr = np.arange(12).reshape((4, 3))
    perm = np.random.permutation(arr)
    print(perm)


def thrd():
    gmt = np.random.geometric(0.65, 1000)
    count, bins, ignored = plt.hist(gmt, 40, density=True)
    plt.show()


if __name__ == '__main__':
    fst()
    sec()
    thrd()