names = [("John", "Mike"), "Sophia", ("David", "Chris"), "Emma", "Olivia"]

def count_boy_girl(names) :

    boys = 0
    girls = 0

    for e in names :
        if isinstance(e, tuple) :
            boys += len(e)
        else :
            girls += 1
    return boys,girls

boys,girls = count_boy_girl(names)
print(boys, girls)