def count_vowels(s) :
    if s == "" :
        return 0
    if s[0].lower() in "aeiou" :
        return 1 + count_vowels(s[1:])
    else :
        return count_vowels(s[1:])
    
print(count_vowels("Hello World"))