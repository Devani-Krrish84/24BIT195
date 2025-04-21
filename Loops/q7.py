def factorial(n) :
    fac = 1
    if n == 0 :
        return 1
    for i in range(n, 1, -1) :
        fac *= i
    return fac

def nPr(n ,r) :
    return factorial(n) / factorial(n - r)

def nCr(n, r) :
    return factorial(n) / (factorial(n - r) * factorial(r))

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))   
print("nPr : ", nPr(n, r))
print("nCr : ", nCr(n, r))