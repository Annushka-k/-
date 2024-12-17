def func():
    i = yield
    while True:
        if i >= 0:
            i = yield i ** 0.5
        else:
            i = yield None

generator = func()
next(generator)
numbers = [i for i in range(-5, 10)]
for i in numbers:
    itog = generator.send(i)
    itog = generator.send(i)
    if itog is not None:
        print(itog)