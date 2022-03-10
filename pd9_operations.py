import pandas as pd
import numpy as np


def add(a, b, c):
    return a + b + c


def normalize(x, y):
    x_new = ((x - np.mean([x, y])) / (max(x, y) - min(x, y)))
    return x_new


def fst():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

    df = pd.DataFrame(data)
    func = lambda row: add(row['A'], row['B'], row['C'])
    df['add'] = df.apply(func, axis=1)
    print(f'After Applying Function:\n{df}')


def sec():
    data = {
        'X': [1, 2, 3],
        'Y': [45, 65, 89]
    }

    df = pd.DataFrame(data)
    func = lambda row: normalize(row['X'], row['Y'])
    df['X'] = df.apply(func, axis=1)
    print(f'Normalized:\n{df}')


def thrd():
    df = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv')
    result1 = df.aggregate(['sum', 'min'])
    print(result1, end='\n\n')

    result2 = df.aggregate({
            'Number': ['sum', 'min'],
            'Age': ['max', 'min'],
            'Weight': ['min', 'sum'],
            'Salary': ['sum']
    })
    print(result2, end='\n\n')


def frth():
    df = pd.DataFrame({'A': [12, 4, 5, None, 1],
                       'B': [7, 2, 54, 3, None],
                       'C': [20, 16, 11, 3, 8],
                       'D': [14, 3, None, 2, 6]})

    man = df.mean(axis=0, skipna=True)  # skip the Na values while finding the mean
    md = df.mad(axis=0, skipna=True)
    sm = df.sem(axis=0, skipna=True)

    print(f'mean\n{man}', end='\n\n')
    print(f'mad\n{md}', end='\n\n')
    print(f'sem\n{sm}', end='\n\n')


fst()
sec()
thrd()
frth()


# https://www.geeksforgeeks.org/apply-function-to-every-row-in-a-pandas-dataframe/
# https://www.geeksforgeeks.org/python-pandas-dataframe-aggregate/
# https://www.geeksforgeeks.org/python-pandas-dataframe-mad/