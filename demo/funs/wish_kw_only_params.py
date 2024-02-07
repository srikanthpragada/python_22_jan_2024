# Keyword-only args
def wish(*, user, msg):
    print(msg, user.upper())


# Keyword args
wish(user="Scott", msg="Hello")
wish(msg = "Hi", user = "Bill")