def row(rowIndex):
    string = [1] * (rowIndex + 1)
    for number1 in range(1, rowIndex):
        for number2 in range(number1, 0, -1):
            string[number2] += string[number2 - 1]
    return string
print(row(3))