def unique_element(numbers):
    unique_number=[]

    for number in numbers:
        if number not in unique_number:
            unique_number.append(number)
    return unique_number


numbers=[1,2,3,4,5,6,7,8,9,10]
print(unique_element(numbers))