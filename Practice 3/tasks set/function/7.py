def func(numbers):
    for index in range(len(numbers)-1):
        if numbers[index]==3 and numbers[index+1]==3:
            return True
    return False

print(func([1,3,3]))
print(func([1,3,1,3]))
print(func([3,1,3]))