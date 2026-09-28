celsius = [0, 10, 20, 30, 40]
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print("Fahrenheit:", fahrenheit)

strings = ["hello", "python", "world", "programming"]
def to_uppercase(s):
    return s.upper()
uppercase = list(map(to_uppercase, strings))
print("Uppercase:", uppercase)
#output:-
#Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]
#Uppercase: ['HELLO', 'PYTHON', 'WORLD', 'PROGRAMMING']

