nums = [1, -4, 50, -60]
names = ['abc', 'pqrs', 'xy', 'defgh']

for n in sorted(nums, key=abs):
    print(n)

for n in sorted(names, key=len):
    print(n)
