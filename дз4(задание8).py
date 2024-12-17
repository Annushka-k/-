def fun(stroki):
    for i in stroki:
        if len(i) > 3:
            yield i
stroki = ['124', 'сat', 'python', 'ilya']
print(list(fun(stroki)))