import random

num = [random.randrange(1, 40) for _ in range(21)]

rand = int(input("Enter a number between 1 and 40: "))

def find_occurrence(rand, num) :
    count = []
    for i in range(len(num)) :
        if num[i] == rand :
            count.append(i)
    return count

print(find_occurrence(rand, num))