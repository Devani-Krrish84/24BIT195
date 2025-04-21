def dollars_to_pounds(dollars):
    rs = dollars * 48
    return rs / 70

# Example usage
dollars = float(input("Enter the amount in dollars: "))
print(f"{dollars} dollars is equal to {dollars_to_pounds(dollars)} pounds.")