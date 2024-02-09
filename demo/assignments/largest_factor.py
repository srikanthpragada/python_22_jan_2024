def largest_factor(num):
    for i in range(num // 2, 0, -1):
        if num % i == 0:
            return i


print(largest_factor(55))
print(largest_factor(53))
print(largest_factor(100))

