grade = lambda marks: "Pass" if marks >= 40 else "Fail"
marks = [35, 45, 67, 20, 50, 38]
for mark in marks:
    print(mark, grade(mark))
#output:-
#35 Fail
#45 Pass
#67 Pass
#20 Fail
#50 Pass
#38 Fail
