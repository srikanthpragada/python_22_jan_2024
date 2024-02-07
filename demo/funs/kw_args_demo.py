def fun(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def details(*args, **kwargs):
    pass


fun(a=10, b=20)
fun(n='Abc', e="abc@gmail.com")
details(10, 20, a=100, b='xyz')
