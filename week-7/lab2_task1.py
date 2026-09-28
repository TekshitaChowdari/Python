def Student(name, roll_no, branch):
    print("NAME:", name)
    print("ROLL NO:", roll_no)
    print("BRANCH:", branch)

print("Using positional arguments")
Student("Tekshita", "P9", "D")

print("Using keyword arguments")
Student(branch="D", name="Tekshita", roll_no="P9")    
#output:-
#Using positional arguments
#NAME: Tekshita
#ROLL NO: P9
#BRANCH: D
#Using keyword arguments
#NAME: Tekshita
#ROLL NO: P9
#BRANCH: D
