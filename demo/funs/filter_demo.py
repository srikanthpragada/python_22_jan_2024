nums = [1, 5, 4, 8, 9]


def iseven(n):
    return n % 2 == 0


for n in filter(iseven, nums):
    print(n)
