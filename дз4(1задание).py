n = int(input())
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

fib = list(fibonacci(n))
print(fib)
