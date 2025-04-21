# Write a program that converts words present in a list into uppercase and stores them in a set

list = ["hello", "world", "python", "programming"]

def compute_to_upper(list) :
    upper = {i.upper() for i in list}
    return upper

print(compute_to_upper(list))
