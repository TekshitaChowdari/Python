s=input("enter a String:")
vowels = consonants = digits = spaces = 0
for char in s.lower():
    if char in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print("Vowels:",vowels)
print("consonants:",consonants)
print("digits:",digits)
print("spaces:",spaces)
#output:-
#enter a String:Tekshita Chowdari 1114
#Vowels: 6
#consonants: 10
#digits: 4
#spaces: 2
