def intersection_list(list1, list2) :
    intersection = list(set(list1) & set(list2))
    return intersection

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(intersection_list(list1, list2))