s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)
#OUTPUT:-
#Enter a string: PROGRAMMING
#After removing duplicates: PROGAMIN

