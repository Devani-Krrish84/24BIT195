def is_prime(num) :
    if num <= 2 :
        return False
    for i in range(2, (num // 2) + 1) :
        if num % i == 0 :
            return False
    return True

def is_perfect(num) :
    if num <= 1 :
        return False
    if sum(i for i in range(1, num) if num % i == 0) == num :
        return True
    return False

def is_armstrong(num) :
    n = str(num)
    sum = 0
    for i in n :
        sum += int(i)**3
    if sum == num :
        return True
    return False

def is_palindrome(num) : 
    s = str(num)
    for i in range(len(s) // 2) :
        if s[i] == s[len(s) - i - 1] :
            continue
        else :
            return False
    return True

def is_automorphic(num) :
    n = num ** 2
    if str(num) == str(n)[len(str(n)) - 2 : ] :
        return True
    return False

num = int(input("Enter a number : "))
print("Prime : ", is_prime(num))
print("Perfect : ", is_perfect(num))
print("Armstrong : ", is_armstrong(num))
print("Palindrome : ", is_palindrome(num))
print("Automorphic : ", is_automorphic(num))