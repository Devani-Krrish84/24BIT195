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

def to_toggle(str) :
    toggle = ""
    for char in str :
        if "a" <= char <= "z" :
            toggle += chr(ord(char) - 32) 
        elif "A" <= char <= "Z" :
            toggle += chr(ord(char) + 32)
        else :
            toggle += char
    return toggle

print(to_upper(str))
print(to_lower(str))    
print(to_toggle(str))