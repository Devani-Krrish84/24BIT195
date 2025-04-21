def swap_values(a, b):
    return b, a

# Example usage
a = input("Enter the first value: ")
b = input("Enter the second value: ")
a, b = swap_values(a, b)
print(f"After swapping: First value = {a}, Second value = {b}")