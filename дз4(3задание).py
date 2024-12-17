def gen(lln):
    if lln == 0:
        yield ""
    else:
        for i in gen(lln - 1):
            yield i + 'b'
            yield i + 'a'
def check(lln):
    sum = 0
    for i in gen(lln):
        if 'ab' not in i:
            sum += 1
    return sum
print(check(6))