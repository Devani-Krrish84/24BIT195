list1 = [1, 2, 3, 4, 5]

def reverse_list(list1) :
    if list1 == [] :
        return []
    else :
        return reverse_list(list1[1:]) + [list1[0]]
    
print(reverse_list(list1))