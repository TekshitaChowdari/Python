n = int(input("Enter N: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
#output:-
#Enter N: 5
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
