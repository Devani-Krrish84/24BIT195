def triangle_area(height, base):
    return (height * base) / 2

# Example usage
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area = triangle_area(height, base)
print(f"The area of the triangle is: {area}")