def generate_fibonacci(n):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers[:n]

n = int(input("Enter the value of n: "))
fibonacci_sequence = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are:", fibonacci_sequence)
