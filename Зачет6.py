def reverse(s, k):
    listS = list(s)
    for index in range(0, len(listS), 2 * k):
        listS[index:index + k] = reversed(listS[index:index + k])
    return ''.join(listS)
print(reverse( "abcd", 2))