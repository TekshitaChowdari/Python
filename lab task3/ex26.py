n = int(input("Enter N: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
#output:-
#Enter N: 5
#A 
#A B 
#A B C 
#A B C D 
#A B C D E 
