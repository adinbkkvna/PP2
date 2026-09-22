num=[1,2,3,4,5]
doubled=list(map(lambda x: x*2,num))
print(doubled)

price=[10,20,30,40]
new_price=list(map(lambda x:x*3,price))
print(new_price)

price=[10,20,30,40]
new_price=list(map(lambda price:price+10,price))
print(new_price)
