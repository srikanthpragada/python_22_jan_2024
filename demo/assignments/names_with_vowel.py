names = ["java", "python", "sql", "ruby", "c#"]


def contains_vowel(name):
    for c in name:
        if c in 'aeiou':
            return True

    return False


def contains_vowel_v2(name):
    for c in 'aeiou':
        if name.find(c) >= 0:
            return True

    return False


for n in filter(contains_vowel_v2, names):
    print(n)
