chch = [i for i in range(1, 15)]
def num(chch):
    for i in chch:
        if i % 2 == 0:
            yield i

print(list(num(chch)))