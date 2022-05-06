
A = int(input())
N = int(input())

RES = A**N
print(RES)

if RES < 10:
    print(RES)
else:
    while RES > 10:
        RES = RES / 10
    print(round(RES))