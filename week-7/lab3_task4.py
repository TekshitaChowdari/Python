def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        return base * power(base, exp - 1)
base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result:", power(base, exp))
#output:-
#Enter base: 4
#Enter exponent: 2
#Result: 16.0
