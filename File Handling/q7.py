import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"Employee Code: {self.empcode}, Name: {self.empname}, Date of Joining: {self.doj}, Salary: {self.salary}"

employee = Employee(101, "John Doe", "2023-01-15", 50000)

with open("employee_data.txt", "wb") as file:
    pickle.dump(employee, file)

with open("employee_data.txt", "rb") as file:
    deserialized_employee = pickle.load(file)

print(deserialized_employee)