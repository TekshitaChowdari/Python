s = input("Enter a string: ")

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

print("Reversed string:", reverse)
#output:-
#Enter a string: hello
#Reversed string: olleh
