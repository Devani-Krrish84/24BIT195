import random

# Create a list of 5 odd integers
odd_integers = [random.randrange(1, 100, 2) for _ in range(5)]
print("List of 5 odd integers:", odd_integers)

# Create a list of 4 even integers
even_integers = [random.randrange(0, 100, 2) for _ in range(4)]
print("List of 4 even integers:", even_integers)

# Replace the third element of odd_integers with even_integers list
print("Original odd integers list:", odd_integers)
odd_integers[2] = even_integers
print("After replacing third element with even integers list:", odd_integers)

# Flatten the list
flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print("Flattened list:", flattened_list)

# Sort the flattened list
flattened_list.sort()
print("Sorted flattened list:", flattened_list)