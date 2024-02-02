input_string = input("Enter a string :")

unique_characters = []
for c in input_string:
    if c not in unique_characters:
        unique_characters.append(c)

print(unique_characters)