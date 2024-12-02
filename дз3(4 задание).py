def factorial(n):
    if n > 0:
        return n * int(factorial(n-1))
    else:
        return 1
print(factorial(3))