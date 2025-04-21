def calculate_net_salary(gross_salary):
    allowance = gross_salary * 0.1
    deduction = gross_salary * 0.03
    return gross_salary + allowance - deduction

# Example usage
gross_salary = float(input("Enter the gross salary: "))
net_salary = calculate_net_salary(gross_salary)
print(f"The net salary is: {net_salary}")