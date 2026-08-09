first_name = input("Enter first name: ")
roll_number = input("Enter roll number: ")

username = first_name.lower() + roll_number[-2:]

print("Username:", username)
#output:-
#Enter first name: Tekshita
#Enter roll number: 25341A05P9
#Username: tekshitaP9
