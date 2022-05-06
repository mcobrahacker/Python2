n = int(input())

k = n
a = 1
b = 0

while k != 0:
    if k % 2 == 0:
        l = k / 2
        a = a + b
        k = l
    else:
        l = k / 2
        b = a + b
        k = l

print(n)
print(a)
print(b)