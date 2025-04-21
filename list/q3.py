import random

list = [random.randrange(1,31) for _ in range(51)]

def remove_duplicates(list) :
    res = []

    for i in list :
        if i not in res :
            res.append(i)
    return res

print(remove_duplicates(list))