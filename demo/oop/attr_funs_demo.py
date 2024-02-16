class Person:
    def __init__(self, name):
        self.name = name


p = Person("Rossum")

print(getattr(p, 'name'))
print(hasattr(p, 'age'))
setattr(p, 'age', 20)
print(hasattr(p, 'age'))
delattr(p, 'age')
print(hasattr(p, 'age'))
print(getattr(p, 'gender', 'male'))

