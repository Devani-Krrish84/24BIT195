num = int(input("Enter a number : "))

def mult_table(num) :
    for i in range(1, 11) :
        print(num, "x", i, "=", num * i)

mult_table(num)