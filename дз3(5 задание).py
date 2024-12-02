def power1(a, n):
    if n>0:
        return a * power1(a, n-1)
    else:
        return 1
print(power1(2, 3))