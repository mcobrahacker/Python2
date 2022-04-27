# Составить программу, которая вычисляет внутренние углы треугольника, заданного длинами сторон.

import math

AB = float(input('Введите длину стороны AB: '))
BC = float(input('Введите длину стороны BC: '))

print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')