def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a number: "))
print("Factorial:", factorial(n))
#output:-
#Enter a number: 5
#Factorial: 120
