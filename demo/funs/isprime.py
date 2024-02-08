def isprime(num: int) -> bool:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


if isprime(11):
    print('Prime')
else:
    print('Not Prime')
