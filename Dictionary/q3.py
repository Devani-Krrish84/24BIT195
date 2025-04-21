# List of dictionaries containing department number, roll number, and salary
employees = [
    {"dept_no": 101, "roll_no": 1, "salary": 50000},
    {"dept_no": 102, "roll_no": 2, "salary": 60000},
    {"dept_no": 101, "roll_no": 3, "salary": 70000},
    {"dept_no": 103, "roll_no": 4, "salary": 80000},
    {"dept_no": 102, "roll_no": 5, "salary": 90000},
]

# Dictionary to store department-wise salaries
dept_salaries = {}

# Group salaries by department
for emp in employees:
    dept_no = emp["dept_no"]
    salary = emp["salary"]
    if dept_no not in dept_salaries:
        dept_salaries[dept_no] = []
    dept_salaries[dept_no].append(salary)

# Find min and max salaries for each department
for dept_no, salaries in dept_salaries.items():
    print(f"Department {dept_no}:")
    print(f"  Minimum Salary: {min(salaries)}")
    print(f"  Maximum Salary: {max(salaries)}")

