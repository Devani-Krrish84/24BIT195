def calculate_average_and_total(sub1, sub2, sub3):
    total = sub1 + sub2 + sub3
    average = total / 3
    return total, average

# Example usage
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
total, average = calculate_average_and_total(sub1, sub2, sub3)
print(f"The total marks are: {total}")
print(f"The average marks are: {average}")