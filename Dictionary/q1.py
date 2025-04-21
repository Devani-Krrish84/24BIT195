dict1 = {1:"one", 2: "two", 3: "three"}
dict2 = {4:"four", 5: "five", 6: "six"}
dict3 = {7:"seven", 8: "eight", 9: "nine"}

dict4 = {**dict1, **dict2, **dict3}
print(dict4)