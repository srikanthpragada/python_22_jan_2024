# Print avg of 5 numbers

total = 0
for n in range(5):
    num = int(input("Enter number :"))
    total += num

print(f"Average = {total // 5}")
