import re
import matplotlib.pyplot as plt


file_name = "data_test.txt"

with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

tranzakciya = len(lines) - 1
print(tranzakciya)

sum = 0
for i in lines[1:]:
    x = i.split(',')
    kol = float(x[3].strip())
    sum += kol
print(sum)

electronic = []
for i in lines[1:]:
    if re.search(r'Electronics', i):
        electronic.append(i.strip())
print('Electronics')
for j in electronic:
    print(j)

price_tran = []
for i in lines[1:]:
    x = i.split(',')
    kol = float(x[3].strip())
    if kol > 100:
        price_tran.append(i.strip())
print('с суммой больше 100')
for j in price_tran:
    print(j)

categoryia = {}
for i in lines[1:]:
    x = i.split(',')
    categoryiaegory = x[4].strip()
    if categoryiaegory in categoryia:
        categoryia[categoryiaegory] += 1
    else:
        categoryia[categoryiaegory] = 1

plt.figure(figsize=(7, 5))
plt.bar(categoryia.keys(), categoryia.values(), color='red', edgecolor='black')
plt.xlabel('категория', fontsize=10)
plt.ylabel('количество покупок', fontsize=10)
plt.grid(True)
plt.show()
