str = "JAVATPOINT"
str1 = " world"
i = 100
frmt = "{} is necessary in this {}".format(str, str1)

print(str[0])
print(str[0:])
print(str[:3])
print(str[1:5])

print(str * 3)
print(str + str1)
print(r"C://python37")
print("The string : %s %d" % (str, i))

print(frmt)

x = "hello"
y = "OK"
z = "a1b2c3"
u = "123"

print(x.capitalize())
print(x.upper())
print(y.lower())
print(z.isalnum())
print(x.isalpha())
print(u.isdecimal())
print(u.isdigit())
print(u.isnumeric())
print(x.islower())
print(y.isupper())
print(len(x))

w = 'xyz aaa bb aaa cdefgh'

print(w.count('aaa', 0, len(w)))
print(w.find('aaa', 0, len(w)))
print(w.replace('aaa', 'ggg'))

# Strings are immutable in Python
