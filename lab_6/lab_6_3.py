n = int(input())

k = n

while k!=1 :
    l = 2
    while k % l != 0:
        l = l + 1
    print(l)
    k = k / l
