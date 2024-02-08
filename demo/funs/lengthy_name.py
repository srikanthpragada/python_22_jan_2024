
def lengthy_name(*names: object) -> object:
    largest = names[0]
    for n in names[1:]:
        if len(n) > len(largest):
            largest = n

    return largest   # return a value 


ln = lengthy_name('Java', 'C', 'C#', 'Ruby')





