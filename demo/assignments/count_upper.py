def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


print(count_upper("python"))
print(count_upper("JAVA"))
print(count_upper("JavaScript"))

