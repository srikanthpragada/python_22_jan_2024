def isprime(num: int) -> bool:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


nums = [1, 5, 9, 15, 23]

for n in filter(isprime, nums):
    print(n)
