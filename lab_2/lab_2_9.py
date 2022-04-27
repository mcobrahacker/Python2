# Написать программу решения задачи: найти длины биссектрис треугольника, заданного координатами своих вершин A, B, C.

from math import sqrt
 
def fun(x, y, z) :
    d = y + z
    return sqrt(y * z * (d + x) * (d - x)) / d
    
a = float(input('введите a: '))
b = float(input('введите b: '))
c = float(input('введите c: '))

print('Биссектриса к "a" = {:f}'.format(fun(a, b, c)))
print('Биссектриса к "b" = {:f}'.format(fun(b, c, a)))
print('Биссектриса к "с"= {:f}'.format(fun(c, a, b)))