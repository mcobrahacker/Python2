# Написать программу решения задачи: найти длины медиан треугольника, заданного координатами своих вершин A, B, C.

from math import sqrt
 
 
def med(x, y, z):
    return sqrt(2 * (x * x + z * z) - y * y) / 2

a, b, c, = map(float, input().split())
m1 = med(a, b, c)
m2 = med(b, a, c)
m3 = med(a, c, b)