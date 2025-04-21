def generate_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_series = generate_fibonacci(n)
if fibonacci_series:
    print(f"The first {n} numbers of the Fibonacci series are: {fibonacci_series}")