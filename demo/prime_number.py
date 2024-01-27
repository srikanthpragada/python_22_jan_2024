# Print whether a number is prime or not

num = int(input("Enter a number :"))
prime = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print('Not prime')
        prime = False
        break

if prime:
    print("Prime Number")
