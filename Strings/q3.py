str1 = "krrish"
str2 = "devanikrrish"

def check_string(str1, str2) :
    if str1 in str2 :
        return True
    return False

print(check_string(str1, str2))