# Print factors for the given number

num = int(input("Enter a number :"))
total = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        total += i

print(total)


