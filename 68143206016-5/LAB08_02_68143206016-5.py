employees = [
    ["Alice", 40, 150],
    ["Bob", 35, 160],
    ["Charlie", 45,155],
    ["David", 50, 140],
    ["Eve", 38, 175],
    ["Frank", 42, 165]
]

for r in range(len(employees)):
    salary = employees[r][1] * employees[r][2]
    print(f"{employees[r][0]} : {salary}")