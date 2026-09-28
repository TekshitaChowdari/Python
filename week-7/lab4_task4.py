numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubes = list(map(lambda x: x ** 3, numbers))
divisible = list(filter(lambda x: x % 3 == 0, numbers))
print("Cubes:", cubes)
print("Divisible by 3:",divisible)
#output:-
#Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729]
#Divisible by 3: [3, 6, 9]
