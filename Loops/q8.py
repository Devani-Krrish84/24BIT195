def factorial(n) :
    fac = 1 
    if n == 0 :
        return 1
    for i in range(n, 1, -1) :
        fac *= i
    return fac

num = int(input("Enter a number : "))
print("Factorial : ", factorial(num))