num = int(input("Enter a number: "))

temp = num
sum = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit
    count = count + 1
    temp = temp // 10

average = sum / count

print("Sum of digits:", sum)
print("Average of digits:", average)
#output:-
#Enter a number: 12345
#Sum of digits: 15
#Average of digits: 3.0
