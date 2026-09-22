numbers=[1,2,3,4,5,6,7,8,9,10]

prime_numbers=list(filter(
    lambda number: number>1 and all(number%divisor!=0
        for divisor in range(2,int(number**0.5)+1)),numbers))
print(prime_numbers)