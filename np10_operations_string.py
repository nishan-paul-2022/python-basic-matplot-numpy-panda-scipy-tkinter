import numpy as np
from numpy import char as man


if __name__ == '__main__':
    print('lower: ', man.lower(['Geeks', 'For']))
    print('upper: ', man.upper(['Geeks', 'For']))
    print('capitalize: ', man.capitalize(['Geeks', 'For']))
    print('split: ', man.split('geeks for geeks'))
    print('split: ', man.split('geeks, for, geeks', sep=','))
    print('join: ', man.join('-', 'geeks'))
    print('join: ', man.join(['-', ':'], ['geeks', 'for']))

    a = np.array(['geeks', 'for', 'geeks'])
    print('count: ', man.count(a, 'geek'))
    print('count: ', man.count(a, 'fo'))

    print('isalnum: ', man.isalnum('geeks'))
    print('equal: ', man.equal('geeks', 'for'))
    print('greater: ', man.greater('geeks', 'for'))
    print('less: ', man.less('geeks', 'for'))
    print('greater_equal: ', man.greater_equal('geeks', 'for'))
    print('less_equal: ', man.less_equal('geeks', 'for'))

# https://www.geeksforgeeks.org/numpy-string-operations/