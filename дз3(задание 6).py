def obrat():
    num=int(input())
    if num != 0:
        obrat()
    print(num)
obrat()