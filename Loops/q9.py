def print_natural_num(n) :
    for i in range(n, 0, -1) :
        print(i, end = ", ")

n = int(input("Enter a number : "))
print_natural_num(n)