tup = (1, 2, 3, 4, 5)
print(f"Tuple Before : {tup}")
list = list(tup)
list[2] = 10
tup = tuple(list)
print(f"Tuple After : {tup}")