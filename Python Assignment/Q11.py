n=int(input("enter n: "))
fibonacci = [0, 1]
for i in range(2, n):
    next_fib = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fib)

# Print the Fibonacci sequence
print(f"The first {n} Fibonacci numbers are:")
print(fibonacci)