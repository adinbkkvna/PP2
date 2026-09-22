def func(*args):
    print("Type",type(args))
    print("First",args[0])
    print("Second", args[1])
    print("Third", args[2])
    print("All", args)
func("Emil","Adina","Amina")

#using *args with regular func
def func(greeting, *names):
    for name in names:
        print(greeting,name)
func("Hello","Adina","Amina")


def func(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(func(1, 2, 3))
print(func(10, 20, 30, 40))
print(func(5))


#**kwargs
def func(**info):
   print("Type",type(info))
   print("Name",info["name"])
   print("Age", info["age"])
   print("All", info)
func(name="Adina",age="19",city="Almaty")
   

#combine
def func(title,*args,**kwargs):
   print("Title", title)
   print("Positional arg", args)
   print("keyword arg",kwargs)
func("User info","Adina","Amina",age=19,city="Aktobe")