# Составить алгоритм и разработать программу, которая находит последние две цифры произведения четырех натуральных чисел А, В, С, D.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = a * b * c * d

print(result % 100)