# Разработать алгоритм и реализовать программу, дающую ответ на вопрос: находится ли пешка под боем коня. 
# Белый конь расположен на поле (х, n). Черная пешка расположена на поле (y, m). 

print("Расположение фигурки коня (1 - 8): ")
A1 = int(input("A1 - "))
B1 = int(input("B1 - "))
print("Расположение точки пешки (1 - 8): ")
A2 = int(input("A2 - "))
B2 = int(input("B2 - "))

if (abs(A1-A2) == (abs(B1-B2))):
    print("Да!")
else:
    print("Нет!")