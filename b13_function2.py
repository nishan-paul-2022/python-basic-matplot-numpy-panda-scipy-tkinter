def f(m):
    return m['value']


def g(m):
    return len(m)


x = [5, 1, 7, 3, 9, 2, 0, 4, 8, 6]
x.sort(reverse=True)
print(x)
x.sort()
print(x)

y = [{'name': 'a', 'value': 500}, {'name': 'b', 'value': 100}, {'name': 'c', 'value': 50}, {'name': 'd', 'value': 350},
     {'name': 'e', 'value': 200}, {'name': 'f', 'value': 150}, {'name': 'g', 'value': 450}, {'name': 'h', 'value': 300}]

y.sort(key=f)
print(y)
y.sort(key=f, reverse=True)
print(y)

z = ["hello", "mega", "google", "bmw", "batman", "superman"]
z.sort()
print(z)
z.sort(key=g)
print(z)
