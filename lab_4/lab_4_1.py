# Даны предметы A, B, C весящие соответственно pA, pB, pC гр. Составить алгоритм и разработать программу упорядочения этих предметов по весу. 
# Алгоритм должен использовать операции сравнения весов двух предметов, называемые взвешиваниями. 
# Количество взвешиваний, выполняемых алгоритмом, должно быть минимальным  

pA = int(input("Введите вес A: "))
pB = int(input("Введите вес B: "))
pC = int(input("Введите вес C: "))

X = 1

if pA > pB:
    if pB > pC:
        X = pA
        pA = pC
        pC = X
    else:
        if pC < pA:
            X = pA
            pA = pB
            pB = pC
            pC = X
        else:
            X = pB
            pB = pA
            pA = X
else:
    if pC < pA:
        X = pB
        pB = pA
        pA = pC
        pc = X
    elif pC < pB:
        X = pB
        pB = pC
        pC = X

print(pA,pB,pC)    

