import re
import matplotlib.pyplot as plt

file_path = 'data.txt'

dates = []
temperatures = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # извлечение даты и температуры
        match = re.search(r'(\d{4}-\d{2}-\d{2}): Temperature = (\d+)°C', line)
        if match:
            dates.append(match.group(1))  # Первая группа — дата
            temperatures.append(int(match.group(2)))  # Вторая группа — температура


plt.figure(figsize=(6, 7))
plt.hist(temperatures, bins=range(min(temperatures), max(temperatures)), edgecolor='red')
plt.xlabel('Температура', fontsize=10)
plt.grid(True)
plt.show()
