# Take numbers until 0 and display sum of numbers

total = 0 
while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break      # stop loop

    total += num


print("Total = ", total)


