#Составить алгоритм и разработать программу, которая находит последние четыре цифры 32-ой степени натурального числа N. (N32)

def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))

N = int(input("Введите число: "))
print(power(N, 32) % 10000)