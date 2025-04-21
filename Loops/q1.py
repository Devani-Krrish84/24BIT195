str = input("Enter a String : ")

def to_upper(str) :
    upper = ""
    for char in str :
        if "a" <= char <= "z" :
            upper += chr(ord(char) - 32)
        else :
            upper += char
    return upper

def to_lower(str) :
    lower = ""
    for char in str :
        if "A" <= char <= "Z"  :
            lower += chr(ord(char) + 32)
        else :
            lower += char
    return lower

print("Upper Case : ", to_upper(str))
print("Lower Case : ", to_lower(str))