# Построить математическую модель и составить программу 
# расчета координат материальной точки, пущенной с начальной скоростью V0 под углом Alfa 
# к горизонту в направлении вектора а = (X0,Y0) в момент времени t.

import math

t = float(input("Время: "))

V0 = float(input("Начальная скорость: "))
Alpha = int(input("Угол: "))

VX = V0 * math.cos(Alpha)
VY = V0 * math.sin(Alpha)

print("Vx - ", VX)
print("Vy - ", VY)

X = t * VX
Y = VY * t - (10 * (t*t))/2

print("Х - ", X)
print("Y - ", Y)