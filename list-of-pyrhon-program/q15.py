def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

# Example usage
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius}°C.")