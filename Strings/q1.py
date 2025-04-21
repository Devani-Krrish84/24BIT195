str = input("Enter a String : ")

def count_vowels(str) :
    count = 0
    for i in str :
        if i in "aeiou" :
            count += 1
    return count

print(count_vowels(str))