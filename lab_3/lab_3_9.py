# Разработать алгоритм и реализовать программу, дающую ответ на вопрос: является ли  одно из двух
#  данных натуральных чисел M и N квадратом другого.

def IS(NUM):
    i = 1
    while i*i <= NUM:
        i = i + 1
    if i*i == NUM:
        return 1
    else:
        return 0
num = int(input())

if(IS(num)):
    print("YES")
else:
    print("NO")
