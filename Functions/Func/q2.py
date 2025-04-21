def compute(num) :
    s = str(num)

    result = int(s) + int(s*2) + int(s*3) + int(s*4)

    return result

num = int(input("Enter a number"))
print(compute(num))