s=0
n=int(input())
for i in range(2,n+1):
    check = 1
    for j in range(2, i):
        if i % j ==0:
            check = 0
    if check==1:
        s=s+i