def celsius_to_fahrenheit(celsius):
    return (9 / 5 * celsius) + 32

# Example usage
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F.")