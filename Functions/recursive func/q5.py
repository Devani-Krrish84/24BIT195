def a_power_b(a, b) :
    if b == 0 :
        return 1
    return a * a_power_b(a, b - 1)


a = int(input("Enter a number: "))
b = int(input("Enter its power: "))

print(f"{a} raised to the power {b} is {a_power_b(a, b)}")