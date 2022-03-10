import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fst():  # demonstrate statistical function
    weight = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45])  # construct a weight array

    print('Minimum and maximum weight of the students: {} {}'.format(np.amin(weight), np.amax(weight)))  # minimum and maximum
    print('Range of the weight of the students: ', np.ptp(weight))  # range of weight i.e. max weight-min weight
    print('Weight below which 70 % student fall: ', np.percentile(weight, 70))  # percentile
    print('Mean weight of the students: ', np.mean(weight))  # mean
    print('Median weight of the students: ', np.median(weight))  # median
    print('Standard deviation of weight of the students: ', np.std(weight))  # standard deviation
    print('Variance of weight of the students: ', np.var(weight))  # variance
    print('Average weight of the students: ', np.average(weight))  # average


def sec(f1, f2):
    in_array = np.linspace(-np.pi, np.pi, 10)
    out_array1 = f1(in_array)
    out_array2 = f2(out_array1)

    plt.plot(in_array, out_array1, color='blue', marker=".")  # blue for f1
    plt.plot(in_array, out_array2, color='red', marker='+')  # red for f2
    plt.title('blue : {} | red : {}'.format(f1, f2))
    plt.xlabel('X'), plt.ylabel('Y')
    plt.show()


def thrd():
    angles = np.array([0, 30, 45, 60, 90, 180])
    radians = np.deg2rad(angles)
    degs = np.rad2deg(radians)
    print('Degrees: ', degs)

    base, height = 4, 3
    hvalue = np.hypot(base, height)  # hypot function demonstration | sqrt(x ** 2 + y ** 2)
    print('hypotenuse of right triangle is: ', hvalue)

    leg1 = np.random.rand(3, 4)
    leg2 = np.ones((3, 4))
    result = np.hypot(leg1, leg2)
    print("Hypotenuse is as follows :", result)


def frth():
    in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
    print('input array: ', in_array)
    print('rounded values: ', np.round_(in_array))
    print('flooring: ', np.floor(in_array))
    print('ceiling: ', np.ceil(in_array))

    in_array = [.53, 1.54, .71]
    print('input array: ', in_array)
    print('rounded values: ', np.round_(in_array))

    in_array = [.5538, 1.33354, .71445]
    print('input array: ', in_array)
    print('rounded values (up to 3): ', np.round_(in_array, decimals=3))


def fifth():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    arr1 = [np.NAN, 2, 3, 4, np.NAN]
    arr2 = [-1, 2, 3, -4, -5]

    print('sqrt: ', np.sqrt(arr))
    print('cbrt: ', np.cbrt(arr))
    print('square: ', np.square(arr))
    print('log: ', np.log(arr))
    print('log2: ', np.log2(arr))
    print('log10: ', np.log10(arr))
    print('exp: ', np.exp(arr))
    print('exp2: ', np.exp2(arr))
    print('absolute: ', np.absolute(arr))
    print('max: ', np.max(arr))
    print('min: ', np.min(arr))
    print('nan_to_num: ', np.nan_to_num(arr1))
    print('negative: ', np.negative(arr2))
    print('clip: ', np.clip(arr, a_min=2, a_max=6))
    print('conj: ', np.conj(2 + 4j))
    print('isreal: ', np.isreal([1 + 1j, 0j]))


def sixth():
    in_arr1 = np.array([[2, -7, 5], [-6, 2, 0]])
    in_arr2 = np.array([[5, 8, -5], [3, 6, 9]])

    print('add : ', np.add(in_arr1, in_arr2))
    print('true_divide : ', np.true_divide(in_arr1, in_arr2))
    print('floor_divide : ', np.floor_divide(in_arr1, in_arr2))
    print('float_power : ', np.float_power(in_arr1, in_arr2))


def seventh():
    arr1 = [120, 24, 42, 10]
    arr2 = [2250, 12, 20, 50]
    print('gcd(arr1, arr2): ', np.gcd(arr1, arr2))
    print('gcd(arr1, 10): ', np.gcd(arr1, 10))
    print('mod(arr1, arr2): ', np.mod(arr1, arr2))
    print('remainder(arr1, arr2): ', np.remainder(arr1, arr2))

    data = [75, 69, 56, 46, 47, 79, 92, 97, 89, 88, 36, 96, 105, 32, 116, 101, 79, 93, 91, 112]
    datam = np.mean(data)
    dataa = np.absolute(data - datam)
    print('absolute mean deviation', np.mean(dataa))
    print('sum(data): ', np.sum(data))
    print('std(data): ', np.std(data))
    print('var(data): ', np.var(data))
    print('mean(data): ', np.mean(data))

    df = pd.DataFrame(data)  # Creating data frame of the given data
    print('absolute mean deviation', df.mad())  # mad() is absolute mean deviation function |


if __name__ == '__main__':
    fst()
    sec(np.sin, np.arcsin)
    sec(np.cos, np.arccos)
    sec(np.tan, np.arctan)
    sec(np.sinh, np.arcsinh)
    sec(np.cosh, np.arccosh)
    sec(np.tanh, np.arctanh)
    thrd()
    frth()
    fifth()
    sixth()
    seventh()

# https://www.geeksforgeeks.org/numpy-mathematical-function/
# https://www.geeksforgeeks.org/absolute-deviation-and-absolute-mean-deviation-using-numpy-python/