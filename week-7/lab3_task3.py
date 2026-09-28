def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
def reverse_number(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(reverse_number(n // 10)))
n = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(n))
print("Reverse of number:", reverse_number(n))
#output:-
#Enter a number: 14
#Sum of digits: 5
#Reverse of number: 41
