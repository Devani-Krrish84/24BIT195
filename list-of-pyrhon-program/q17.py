def square_area_perimeter(length):
    area = length ** 2
    perimeter = 4 * length
    return area, perimeter

# Example usage
length = float(input("Enter the side length of the square: "))
area, perimeter = square_area_perimeter(length)
print(f"The area of the square is: {area}")
print(f"The perimeter of the square is: {perimeter}")