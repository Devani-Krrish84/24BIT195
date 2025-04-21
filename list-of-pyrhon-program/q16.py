def calculate_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Example usage
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))
interest = calculate_interest(principal, rate, time)
print(f"The interest is: {interest}")