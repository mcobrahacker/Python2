def PointsCover(S):
    tmp = 0
    while S:
        k = min(S) + 1
        i = 0
        while i < len(S):
            if S[i] < k:
                del S[i]
            else:
                i += 1
        tmp += 1
    return tmp

def PointsCoverSort(S):
    S.sort()
    n = len(S)
    tmp = i = 0
    while i < n:
        tmp += 1
        r = S[i] + 1
        while i < n and S[i] <= r:
            i += 1
    return tmp