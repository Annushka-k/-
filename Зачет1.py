#Напишите программу, которая принимает на вход фразу и составляет аббревиатуру по первым буквам слов:
#Today I learned → TIL Высшее учебное заведение → ВУЗ Кот обладает талантом → КОТ Если слово начинается не с буквы, игнорируйте его:
#Ар 2 Ди #2 → АД Разделителями слов считаются только пробельные символы. Дефис, дробь и прочие можно не учитывать:
#Анна-Мария Волхонская → АВ

string=input()
string=string.upper()
list_of_words=string.split()
for words in range(len(list_of_words)):
    print(list_of_words[words][0], end='')