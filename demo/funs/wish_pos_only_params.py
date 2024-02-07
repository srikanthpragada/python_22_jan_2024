# Positional-only args
def wish(user, message, /):
    print(message, user.upper())


# Positional Args
wish('Jack', 'Hi')


