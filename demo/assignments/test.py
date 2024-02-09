def uppercase_name(name):
    for n in name[1:]:
        if n.isupper():
            n.append()

    return uppercase_name(name)


ln = uppercase_name('aDFGsdf')