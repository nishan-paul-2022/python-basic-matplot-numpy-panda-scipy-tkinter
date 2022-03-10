class OMG:
    def __init__(self, country="BD", ID=1604085):
        self.country = country
        self.ID = ID


class HOW(OMG):
    age = 22
    name = "TDK"


def A():
    x = HOW()
    setattr(x, "age", 25)
    age = getattr(x, "age")
    print(age)


def B():
    x = OMG()
    print("vars: ", vars(x))
    print("isinstance: ", isinstance(x, OMG))
    print("issubclass: ", issubclass(HOW, OMG))


A()
B()
