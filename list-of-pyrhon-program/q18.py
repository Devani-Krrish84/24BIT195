def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

# Example usage
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area, perimeter = rectangle_area_perimeter(length, breadth)
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")