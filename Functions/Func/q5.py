def pangram(sentencs) :
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in alpha :
        if i not in sentencs :
            return False
    return True

print(pangram("The quick brown fox jumps over the lazy dog"))