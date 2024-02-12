g = 100  # Global variable


def f1():
    a = 10  # enclosing variable
    global g
    g = 200
    # local function
    def f2():
        b = 20  # local variable
        nonlocal a
        a = 20
        print(a, b, g)

    f2()
    print(a)


f1()
print(g)
