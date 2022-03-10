def A():
    employee = {"name": "John", "age": 29, "salary": 25000, "company": "GOOGLE"}
    print(employee)

    print("name: ", employee["name"])
    print("age: ", employee["age"])
    print("salary: ", employee["salary"])
    print("company: ", employee["company"])

    dictio = dict([(1, 'Devansh'), (2, 'Sharma')])
    print(dictio)


def B():
    dictio = {0: 'Peter', 2: 'Joseph', 3.5: 'Ricky', 'emp_ages': (20, 33, 24), 'name': 'JavaTpoint'}
    print(dictio)


def C():
    employee = {"name": "John", "age": 29, "salary": 25000, "company": "GOOGLE"}
    value = employee.pop("salary")
    print(value)
    print(employee)


def D():
    employee = {"name": "John", "age": 29, "salary": 25000, "company": "GOOGLE"}
    k = employee.keys()
    v = employee.values()

    for i in k:
        print(i, end=' ')
    print("\n---")

    for i in v:
        print(i, end=' ')
    print("\n---")

    for i in employee:
        print(i, ": ", employee[i])


def E():
    omg = {1: 'a', 2: 'b', 3: 'c'}
    mg = {3: 'd', 5: 'e', 6: 'f'}
    omg.update(mg)
    print(omg)


A()
B()
C()
D()
E()

# Dictionary is mutable
