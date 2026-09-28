students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]
students = sorted(students, key=lambda s: s[1], reverse=True)
print(students)
words = ["apple", "cat", "banana", "dog", "elephant"]
words = sorted(words, key=lambda x: len(x))
print(words)
#output:-
#[('Sita', 92), ('Ravi', 78), ('Amit', 65)]
#['cat', 'dog', 'apple', 'banana', 'elephant']

