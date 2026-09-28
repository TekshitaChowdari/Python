def greet(name):
    return "Hello " + name
f = greet
print(f("Tekshita"))

def display(func, name):
    print(func(name))

display(greet, "Chowdari")

def create_greeting():
    def message(name):
        return "Welcome " + name
    return message

new_func = create_greeting()
print(new_func("Tekshita"))
#output:-
#Hello Tekshita
#Hello Chowdari
#Welcome Tekshita
