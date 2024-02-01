nums = []

while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    nums.append(n)

for n in nums:
    if n % 2 == 0:
        print(n, end=' ')
