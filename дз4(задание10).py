def hehe(s):
    flag = set()
    for i in s:
        if i not in flag and i != ' ' and i != ')':
            flag.add(i)
            yield i

print(list(hehe('не ругайте за решение, пожалуйста)')))