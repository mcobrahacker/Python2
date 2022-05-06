import random

a=list()

for i in range (0,20):
  a.append(random.randint(-20,20))

print('Массив ',a,"\n")

min = a[-20]

for i in range(len(a)):
  if (a[i] < min):
    min = a[i]
    k=i

print(k)
print('Минимальное значение: ',min)