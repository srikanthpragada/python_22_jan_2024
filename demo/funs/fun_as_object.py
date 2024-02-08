def fun():
    print('Function')


f2 = fun
fun()
f2()
print(type(fun))
print(id(fun))
print(id(f2))

a = 100
print(id(a))
