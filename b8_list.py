a = [1, 2, "Peter", 4.50, "Ricky", 5, 6]
b = [1, 2, "Peter", 4.50, "Ricky", 5, 6]
dept = ["CS", 10]
lst = [1, 2, 3, 4, 5, 6, 7, 20]

print(a == b)

print("name : %s, ID: %d" % (dept[0], dept[1]))

print(lst[0])
print(lst[0:5])
print(lst[0:])

lst[2] = 10
lst.remove(20)  # value
lst.append(200)

print(lst * 2)
print(lst + dept)
print(1 in lst)

print(len(lst))
print(max(lst))
print(min(lst))

# list is mutable
