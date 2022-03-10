def A():
    days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
    print(days)

    for i in days:
        print(i, end=' ')
    print()


def B():
    months = {"A", "B", "C", "D", "E", "F"}

    months.remove("A")

    months.add("G")
    months.update({"H", "I"})
    print(months)

    months.pop()
    print(months)

    months.clear()
    print(months)


def C():
    x = {1, 2, 3}
    y = {1, 2, 3, 4, 5, 6}
    z = {4, 5, 6, 7, 8, 9}

    print(x | y | z)  # union
    print(x & y)  # intersection
    print(y ^ z)  # symmetric difference
    print(y - z)  # difference


A()
B()
C()

# Set is unorderd, doesn't allow repeatation, and mutable
