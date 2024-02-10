def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Example usage:
fibonacci_function = caching_fibonacci()

# Calculate Fibonacci numbers with caching
result_10 = fibonacci_function(10)
result_5 = fibonacci_function(5)
result_3 = fibonacci_function(3)

print(result_10)  # Output: 55
print(result_5)   # Output: 5
print(result_3)   # Output: 2
