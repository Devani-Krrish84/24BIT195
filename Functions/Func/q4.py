# Write a program that defines a function sum_avg() to accept marks of five subjects and calculates total and average. It should return directly both values.

def sum_avg(num1, num2, num3, num4, num5) :
    total = num1 + num2 + num3 + num4 + num5
    avg = total / 5
    return total, avg

print(sum_avg(10, 20, 30, 40, 50))
