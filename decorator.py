def protected(func):

    def wrapper(password):

        if password == "platzi":
            return func()
        else:
            print("Your password is incorrect")

    return wrapper

@protected
def protected_func():
    print("Your password is correct")

if __name__ == "__main__":
    password = str(raw_input("Please type in your password: "))

    wrapper = protected(protected_func)

    protected_func(password)