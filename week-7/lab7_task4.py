def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def greeting():
    print("Hello! Welcome!")

greeting()
#output:-
#Hello! Welcome!
#Hello! Welcome!
#Hello! Welcome!
