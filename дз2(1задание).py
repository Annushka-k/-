a = input()
cas = {')':'(',
       ']':'[',
       '}':'{'}
m=[]
for i in a:
    if i in cas.values():
        m.append(i)
    elif i in cas.keys():
        if m==[] or cas[i]!=m.pop():
            print('False')
            exit()
print('True')