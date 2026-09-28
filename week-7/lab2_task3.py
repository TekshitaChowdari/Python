def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


print("3 Marks:")
total, average = total_marks(80, 75, 90)
print("Total:", total)
print("Average:", average)

print("\n5 Marks:")
total, average = total_marks(80, 75, 90, 85, 70)
print("Total:", total)
print("Average:", average)

print("\n1 Mark:")
total, average = total_marks(80)
print("Total:", total)
print("Average:", average)
#output:-
#3 Marks:
#Total: 245
#Average: 81.66666666666667

#5 Marks:
#Total: 400
#Average: 80.0

#1 Mark:
#Total: 80
#Average: 80.0
