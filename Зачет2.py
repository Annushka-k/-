#Напишите программу, которая считает, сколько раз каждая цифра встречается в числе. Гарантируется, что на вход подаются только положительные целые числа, не выходящие за диапазон int.
number=int(input())
count_figure_number=0
count_figure=0
number_test1=number
number_test2=number
while number_test1//10!=0:
    count_figure_number+=1
    number_test1//=10
count_figure_number+=1
for figure in range(0,10):
    count_figure = 0
    number = number_test2
    for _ in range(count_figure_number):
        if number%10==figure:
            count_figure+=1
        number=number//10
    print('Цифра', figure, 'встречается в числе', count_figure, 'раз')


