class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Radius = {self.r}'

    def __eq__(self, other):
        return self.r == other.r

    def __gt__(self, other):
        return self.r > other.r

    def __int__(self):
        return self.r

c1 = Circle(10)  # c1.__init__(10)
c2 = Circle(10)
c3 = Circle(20)

print(str(c1))  # c1.__str__()
print(c1 == c2)  # c1.__eq__(c2)
print(c3 > c2)  # c3.__gt__(c2)
print(c1 < c2)

print(int(c1))   # c1.__int__()