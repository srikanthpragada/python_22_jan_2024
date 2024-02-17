class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __lt__(self, other):
        # print(self, other)
        return self.name < other.name


persons = [Person('A', 20),
           Person('C', 22),
           Person('D', 18),
           Person('B', 19),
           ]

# default order
for p in sorted(persons):
    print(p)

# Custom order
for p in sorted(persons, key=lambda p: p.age):
    print(p)
