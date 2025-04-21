def factorial(n) :
    fac = 1
    if n == 0 :
        return 1
    for i in range(n, 1, -1) :
        fac *= i
    return fac

def calculate_sine(x, terms = 10) :
    sinx = 0
    for n in range(terms) :
        term = (((-1) ** n) * (x ** (2 * n + 1))) / factorial(2 * n + 1)
        sinx += term
    return sinx

degree = float(input("Enter the angle : "))
x = degree * (3.14 / 180)

print(calculate_sine(x))