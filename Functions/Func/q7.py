def palindrome(s) :
    
    for i in range(len(s) // 2) :
        if (i != s[len(s)-i-1]) :
            return True
    return False

print(palindrome("bob"))