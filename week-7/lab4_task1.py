square = lambda n: n * n
even = lambda n: n % 2 == 0
larger = lambda a, b: a if a > b else b
print("Square:", square(5))
print("Is Even:", even(4))
print("Larger:", larger(10, 20))
#output:-
#Square: 25
#Is Even: True
#Larger: 20
