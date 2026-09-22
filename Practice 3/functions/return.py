def func(x,y):
    return x+y
result=func(5,5)
print(result)


def func():
    return ["apple","banana","orange"]
fruits=func()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def func():
    return(10,20)
x,y=func()
print("x:",x)
print("y",y)


def func(number):
    return number%2==0
print(func(10))
print(func(13))