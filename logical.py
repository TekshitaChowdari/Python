percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)
#output:-
#Enter percentage: 12
#Enter attendance %: 75
#Eligible for scholarship: False
