def is_prime(number):
    if number<2:
        return False
    
    for divisor in range(2,int(number**0.5)+1):
        if number%divisor==0:
            return False

    return True; 

def filter_prime(numbers):
    return list(filter(is_prime,numbers))

numbers=[1,2,3,4,5,6,7,8,9,10]
print(filter_prime(numbers))