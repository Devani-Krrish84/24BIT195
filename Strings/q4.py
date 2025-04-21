str1 = "abcdedf"
str2 = "cd"

def remove_string(str1, str2) :
    return str1.replace(str2, "")

print(remove_string(str1, str2))