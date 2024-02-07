def wish(*users, msg='Hi'):
    for u in users:
        print(msg, u)


wish("Scott", "Andy", "Jack", msg="Hello")
wish("Bill", "Dan")
