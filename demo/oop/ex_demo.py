
try:
    num = int(input("Enter number : "))
    print(100 // num)
except ValueError as ex:
    print(f'Error --> {ex}')
# except ZeroDivisionError:
#     print("Zero is not valid!")
finally:
    print("Finally!")


print("The End!")




