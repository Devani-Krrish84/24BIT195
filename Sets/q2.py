# Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.

import random

num = set(random.sample(range(15, 46), 10))

def count_num(num) :
    return sum(1 for i in num if i < 30)

def delete_num(num) :
    return {i for i in num if i <= 35}

count = count_num(num)
delete = delete_num(num)

print("The set of random numbers is: ", num)
print("The count of numbers less than 30 is: ", count)  
print("The set of numbers after deleting those greater than 35 is: ", delete)