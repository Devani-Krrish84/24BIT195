def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

# Example usage
x, y, z = 3, 4, 5
value = int(input("Enter the value to initialize the 3D array: "))
array = create_array(x, y, z, value)
print("3D Array:")
print(array)