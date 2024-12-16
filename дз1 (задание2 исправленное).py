text = input()
r = len(text) - 1
l = 0
asd = 0
while r > l:
    if text[l] != text[r]:
        asd = 1
        break
    l = r + 1
    r = r - 1
if asd == 0:
    print('палиндром')
else:
    print('не палиндром')