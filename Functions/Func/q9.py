def count_alpha_digit(s) :
    alpha = 0
    digit = 0

    for i in s :
        if i.isalpha() :
            alpha += 1
        elif i.isdigit() :
            digit += 1
        
    return {"alpha" : alpha, "digit" : digit}

print(count_alpha_digit("Hello World My name is Devani Krish 123 and i am studing in pdpu"))
     