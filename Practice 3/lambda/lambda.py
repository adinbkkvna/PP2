x=lambda a: a+19
print(x(7))

x=lambda a,b,c : a+b+c
print(x(3,6,9))


def func(n):
    return lambda a: a*n
mydoubler=func(2)
print(mydoubler(11))

def func(n):
    return lambda a:a*n
doubler=func(2)
tripler=func(3)
print(doubler(12))
print(tripler(13))