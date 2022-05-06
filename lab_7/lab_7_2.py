a = [1, 2, 3, 0, 1, 2, 0, 1, 1, 2, 3, 4, 5, 6, 7, 0]
n = len(a)
i = 0
m = 0
while i < n:
    if a[i] == 1:
        j = i
        while j < n-1 and a[j] + 1 == a[j+1]:
            j += 1
        # print(i, j) # начало-конец
        m = max(m, j-i+1)  # макс длина
        i = j
    i += 1
print(*range(1, m+1))