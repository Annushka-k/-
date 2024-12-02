def power(a, n):
    c=a
    for i in range(n-1):
        c = c*a
    print(c)
power(5,3)