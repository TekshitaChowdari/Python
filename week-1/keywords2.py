import keyword

word = input("Enter word: ")

if keyword.iskeyword(word):
    print("Keyword")
else:
    print("Not a Keyword")
    #output:-
#Enter word: class
#Keyword
    
#Enter word: display
#Not a Keyword
