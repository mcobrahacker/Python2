# Разработать алгоритм и реализовать программу, дающую ответ на вопрос: является ли четырехугольник ABCD выпуклым? Точки A, B, C, D заданы своими координатами. 

def point_in(xa, ya, xb, yb, xc,yc,xd,yd) :
        t1 = ((xd - xa)*(yb-ya)-(yd-ya)*(xb-xa))
        t2 = ((xd - xb)*(yc-yb)-(yd-yb)*(xc-xb))
        t3 = ((xd - xc)*(ya-yc)-(yd-yc)*(xa-xc))
        t4 =((xa - xc)*(yb-yc)-(ya-yc)*(xb-xc))
        return t1 * t2 * t3 * t4 > 0
 
 
xa, ya = map(int,input().split())
xb, yb = map(int,input().split())
xc, yc = map(int,input().split())
xd, yd = map(int,input().split())
 
if point_in(xa, ya, xb, yb, xc,yc,xd,yd) :
    print("Выпуклый")
else :
    print("Невыпуклый или не четырехугольник")
