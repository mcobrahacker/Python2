# Разработать алгоритм и реализовать программу, 
# дающую ответ на вопросы: можно ли из отрезков a, b, c составить треугольник и можно ли 
# этот треугольник поместить в круг радиуса R?

import math

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
R = float(input("R: "))

if (A+B>C) and (A+C>B) and (B+C>A):
    P = (A+B+C) / 2
    S = math.sqrt(P*(P-A)*(P-B)*(P-C))
    if (A*B*C)/(4*5) < R:
        print("Возможно")
    else:
        print("Невозможно")
