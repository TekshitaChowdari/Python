from functools import reduce

employees = [
    {"name": "Ravi", "department": "IT", "salary": 30000},
    {"name": "Anu", "department": "HR", "salary": 25000},
    {"name": "Kiran", "department": "IT", "salary": 40000}
]

it_employees = filter(lambda e: e["department"] == "IT", employees)

hiked = map(lambda e: {**e, "salary": e["salary"] * 1.10}, it_employees)

total = reduce(lambda x, e: x + e["salary"], hiked, 0)

print("Total salary after 10% hike:", total)
#output:-
#Total salary after 10% hike: 77000.0
