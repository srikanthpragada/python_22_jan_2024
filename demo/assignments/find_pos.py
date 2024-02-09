
def find_pos(s1, s2):
    for c in s2:
        pos = s1.find(c)
        if pos >= 0:
            return pos

    return -1

print(find_pos('abcd', 'def'))
print(find_pos('abcd', 'efg'))
print(find_pos('abcd', 'fcbg'))


