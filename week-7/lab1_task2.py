def simple_interest(principal, rate, time):

  si=(principal*rate*time)/100
  return si
principal=float(input("enter the princple amount:"))
rate=float(input("enter the rate of intrest:"))
time=float(input("enter time:"))
result=simple_interest(principal, rate, time)
print("Simple Intrest=",result)
#output:-
#enter the princple amount:15000
#enter the rate of intrest:5
#enter time:2
#Simple Intrest= 1500.0
