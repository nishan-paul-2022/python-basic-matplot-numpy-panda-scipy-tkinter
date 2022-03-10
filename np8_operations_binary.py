import numpy as np


def fst():
    in_arr1 = [2, 8, 125]
    in_arr2 = [3, 3, 115]

    out_num = np.bitwise_and(in_arr1, in_arr2)
    print("bitwise_and : ", out_num)

    out_num = np.bitwise_or(in_arr1, in_arr2)
    print("bitwise_or : ", out_num)

    out_num = np.bitwise_xor(in_arr1, in_arr2)
    print("bitwise_xor : ", out_num)

    out_num = np.invert(in_arr1)
    print("invert : ", out_num)

    in_arr = [2, 8, 15]
    bit_shift = [3, 4, 5]

    out_arr = np.left_shift(in_arr, bit_shift)
    print("Output array after left shifting: ", out_arr)

    out_arr = np.right_shift(in_arr, bit_shift)
    print("Output array after right shifting: ", out_arr)


def sec():
    ax = np.array([
        [[1, 0, 1], [0, 1, 0]],
        [[1, 1, 0], [0, 0, 1]]
    ])
    bx = np.packbits(ax, axis=-1)  # packing elements of an array using packbits() function
    print(bx)

    # explaining unpackbits() function
    ay = np.array([[2], [7], [23]], dtype=np.uint8)
    by = np.unpackbits(ay, axis=1)  # packing elements of an array using packbits() function
    print(by)


fst()
sec()

# https://www.geeksforgeeks.org/numpy-binary-operations/