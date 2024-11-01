stack = ["2", "1", "+", "3", "*"]
dop_mas = []
for element_num in range(len(stack)):
    if stack[element_num] == '+':
        dop_mas.append(int(dop_mas[len(dop_mas) - 2]) + int(dop_mas[len(dop_mas) - 1]))
        dop_mas.pop(len(dop_mas) - 2)
        dop_mas.pop(len(dop_mas) - 2)
        continue
    elif stack[element_num] == '-':
        dop_mas.append(int(dop_mas[len(dop_mas) - 2]) - int(dop_mas[len(dop_mas) - 1]))
        dop_mas.pop(len(dop_mas) - 2)
        dop_mas.pop(len(dop_mas) - 2)
        continue
    elif stack[element_num] == '*':
        dop_mas.append(int(dop_mas[len(dop_mas) - 2]) * int(dop_mas[len(dop_mas) - 1]))
        dop_mas.pop(len(dop_mas) - 2)
        dop_mas.pop(len(dop_mas) - 2)
        continue
    elif stack[element_num] == '/':
        dop_mas.append(int(dop_mas[len(dop_mas) - 2]) // int(dop_mas[len(dop_mas) - 1]))
        dop_mas.pop(len(dop_mas) - 2)
        dop_mas.pop(len(dop_mas) - 2)
        continue
    else:
        dop_mas.append(stack[element_num])
print(dop_mas[0])
