year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month < 1 or month > 12:
    print("Invalid Date")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if day >= 1 and day <= 29:
            print("Valid Date")
        else:
            print("Invalid Date")
    else:
        if day >= 1 and day <= 28:
            print("Valid Date")
        else:
            print("Invalid Date")
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <= 30:
        print("Valid Date")
    else:
        print("Invalid Date")
else:
    if day >= 1 and day <= 31:
        print("Valid Date")
    else:
        print("Invalid Date")
#output:-
#Enter year: 2024
#Enter month: 2
#Enter day: 29
#Valid Date
