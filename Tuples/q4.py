import operator

food_items = [("apple", 1.2), ("banana", 0.5), ("orange", 0.8), ("grape", 2.0), ("kiwi", 1.5)]

print(sorted(food_items, key = operator.itemgetter(1), reverse = True))