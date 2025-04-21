def negative_to_positive(list1) :
    if list1 == [] :
        return []
    if list1[0] < 0 :
        return [0] + negative_to_positive(list1[1:])
    else :
        return [list1[0]] + negative_to_positive(list1[1:])
    
list1 = [-1, 2, -3, 4, -5]
print(negative_to_positive(list1))