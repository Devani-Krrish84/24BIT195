str = input("Enter a String : ")

def count_digit_alpha(str) :
    digit = 0
    alpha = 0
    for i in str :
        if i.isdigit() :
            digit += 1
        elif i.isalpha() :
            alpha += 1
    return digit, alpha

digit, alpha = count_digit_alpha(str)
print("Digits : ", digit)
print("Alphabets : ", alpha)