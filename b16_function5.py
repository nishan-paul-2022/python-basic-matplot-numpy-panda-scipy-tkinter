def A():
    code = "x=5\ny=10\nprint('sum =',x+y)"
    exec(code)
    x = 8
    exec('print(x==8)')
    exec('print(x+4)')


def B():
    numList = [4, 5, 6]
    strList = ['four', 'five', 'six']
    result = zip(numList, strList)
    resultDict = dict(result)
    print(resultDict)


def C():
    print(globals()['omg'])
    print(globals()['num'])
    print(globals()['pi'])


omg = "hello"
num = 123
pi = 3.1416

A()
B()
C()
