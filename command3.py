import sys

# Simulate command-line arguments in IDLE
sys.argv = ["command1.py", "10", "20"]

print("Script Name:", sys.argv[0])
print("Number of Arguments:", len(sys.argv) - 1)
print("Arguments:", sys.argv[1:])
#output:-
#Script Name: command1.py
#Number of Arguments: 2
#Arguments: ['10', '20']
