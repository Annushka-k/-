def fibonacci(n):
    number1, number2 = 0, 1
    for _ in range(n):
        yield number1
        number1, number2 = number2, number1 + number2
for num in fibonacci(10):
    print(num)
