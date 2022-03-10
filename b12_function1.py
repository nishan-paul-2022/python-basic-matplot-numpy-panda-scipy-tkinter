def f(*param):
    for i in param:
        print(i, end=' ')
    print()


def g(**param):
    print(param)

    for i in param:
        print(i, ": ", param[i])


f(1, 2, 3, 4)
f(1, 2, 3, 4, 5, 6, 7)

g(a=1, b=2, c=3)
g(a=1, b=2, c=3, d=4, e=5)
