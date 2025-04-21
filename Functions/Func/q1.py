def count_lower_upper(string) :
    lower = 0
    upper = 0

    for i in string :
        if i.islower() :
            lower += 1
        elif i.isupper() :
            upper += 1
    
    return {"lower" : lower, "upper" : upper}

print(count_lower_upper("Hello World My name is Devani Krrish"))