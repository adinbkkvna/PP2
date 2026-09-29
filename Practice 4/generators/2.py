def even(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a value for n: "))

even_numbers = [str(num) for num in even(n)]
print(",".join(even_numbers))