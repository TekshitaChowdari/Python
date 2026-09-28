from functools import reduce

numbers = [2, 4, 6, 8, 10]
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum:", maximum)

words = ["Python", "is", "easy", "to", "learn"]
sentence = reduce(lambda x, y: x + " " + y, words)
print("Sentence:", sentence)
#output:-
#Product: 3840
#Maximum: 10
#Sentence: Python is easy to learn
