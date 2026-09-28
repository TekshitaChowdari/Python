def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(15):
    print(fibonacci(i), end=" ")
print("\n")
count = 0
def check(n):
    global count
    if n == 5:
        count += 1
    if n <= 1:
        return n
    return check(n - 1) + check(n - 2)
check(10)
print("fibonacci(5) is recomputed", count, "times")
#output:-
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
#fibonacci(5) is recomputed 8 times
