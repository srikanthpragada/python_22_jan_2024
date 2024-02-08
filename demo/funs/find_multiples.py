def multiples(*nums, divisor):
    for n in nums:
        if n % divisor == 0:
            print(n)


multiples(10, 20, 35, 33, 45, divisor=5)
