s = input("Enter a string: ")
ch = input("Enter the character to count: ")
count = 0
for i in s:
  if i == ch:
    count += 1
print("Occurrences of", ch, "=", count)
#output:-
#Enter a string: Tekshita chowdari
#Enter the character to count: i
#Occurrences of i = 2
