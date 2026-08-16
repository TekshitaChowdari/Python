start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
#output:-
#Enter starting limit: 18
#Enter ending limit: 30
#19
#23
#29
