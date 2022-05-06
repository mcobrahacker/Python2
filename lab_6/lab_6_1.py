y = int(input('Укажите верхнюю границу: '))
x = int(input('Укажите нижнюю границу: '))
 
for i in range(x,y):
    s = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            s += j
    if s == i:
        print(i)