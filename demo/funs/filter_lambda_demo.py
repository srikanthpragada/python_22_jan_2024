nums = [1, 5, 4, 8, 9]


for n in filter(lambda v: v % 2 == 0, nums):
    print(n)


for n in filter(lambda v: v > 0, nums):
    print(n)