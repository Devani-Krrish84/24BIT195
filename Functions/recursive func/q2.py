def decimal_to_binary(num) :

    if num == 0 :
        return ""
    else :
        return decimal_to_binary(num // 2) + str(num % 2)
    
num = int(input("Enter a number:"))

if num > 0 :
    result = decimal_to_binary(num)
    print(f"The decimal to binary is {result}")
else :
    print("Please enter a positive number")