# Составить программу, которая вычисляет первую цифру числа an (a – действительное число, n – натуральное число.)

import math

def POW(x,y):
    return round(math.exp(y*math.log10(x)))

A = float(input("Число: "))
N = int(input("Степень:"))

C = POW(round(A), N)
X = str(C)

C = int(C / POW(10, len(X)-1))
print(C)