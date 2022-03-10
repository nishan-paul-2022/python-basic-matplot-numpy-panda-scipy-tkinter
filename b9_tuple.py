a = (1, 2, "Peter", 4.50, "Ricky", 5, 6)
b = (1, 2, "Peter", 4.50, "Ricky", 5, 6)
dept = ("CS", 10)
tup = (1, 2, 3, 4, 5, 6, 7, 20)

print(a == b)

print("name : %s, ID: %d" % (dept[0], dept[1]))

print(tup[0])
print(tup[0:5])
print(tup[0:])

print(tup * 2)
print(tup + dept)
print(1 in tup)

print(len(tup))
print(max(tup))
print(min(tup))

# tuple is not mutable
