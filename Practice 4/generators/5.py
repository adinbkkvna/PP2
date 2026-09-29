def count(n):
    for i in range(n,-1,-1):
        yield i

n=int(input())
for x in count(n):
    print(x)