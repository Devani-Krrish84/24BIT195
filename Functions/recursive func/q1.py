def prime_factor(n, divisor = 2) :

    if n == 1 :
        return []
    
    if n % divisor == 0 :
        ans = [divisor] + prime_factor(n // divisor, divisor)
    else :
        ans = prime_factor(n, divisor + 1)

    return ans

print(prime_factor(315))