counter = 0
def wrong_function():
    counter = counter + 1
    print(counter)
try:
    wrong_function()
except UnboundLocalError as e:
    print("Error:", e)
def correct_function():
    global counter
    counter = counter + 1
    print("Counter after using global:", counter)
correct_function()
#Error: cannot access local variable 'counter' where it is not associated with a value
#Counter after using global: 1
