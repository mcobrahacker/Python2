def findWithBarrier(a, key):
    store = a[-1]
    a[-1] = key
    i = 0
    while a[i] != key:
        i += 1
    a[-1] = store
    return i if a[-1] == key or i != len(a) - 1 else -1
    
assert findWithBarrier([1, 2, 3], 1) == 0
assert findWithBarrier([1, 2, 3], 2) == 1
assert findWithBarrier([1, 2, 3], 3) == 2
assert findWithBarrier([1, 2, 3], 0) == -1
assert findWithBarrier([1, 2, 3], 4) == -1