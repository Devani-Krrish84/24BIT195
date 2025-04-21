# Generate the list of 10 different random numbers between -15 and 15. Create a new list by obtaining square of all numbers in a list.

import random

list1 = random.sample(range(-15, 16), 10)
print(list1)

ans = list(map(lambda x: x**2, list1))
print(ans)