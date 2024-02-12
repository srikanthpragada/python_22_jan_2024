def extract_number(s):
    digits = ""
    for c in s:
        if c.isdigit():
            digits += c

    return int(digits)


data = ['ab123', 'xy12pq', '1234', 'dd333']

for n in sorted(data, key=extract_number):
    print(n)
