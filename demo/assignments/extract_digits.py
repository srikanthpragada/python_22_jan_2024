
def extract_digits(s):
    digits =""
    for c in s:
        if c.isdigit():
            digits += c

    return digits


# print(extract_digits('ab12xy89'))
# print(extract_digits('ab12'))
# print(extract_digits('ab'))

data = ['ab123', 'xy12pq45', '123', 'dd333']

for n in map(extract_digits, data):
    print(n)


