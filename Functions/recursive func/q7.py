def average_recursive(numbers, n=None):
    if n is None:
        n = len(numbers)
    if n == 1:
        return numbers[0]
    return (numbers[n - 1] + (n - 1) * average_recursive(numbers, n - 1)) / n

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
result = average_recursive(numbers)
print(f"The average is: {result}")
    