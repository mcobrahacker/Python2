print(*min([tuple(map(int,input().split())) for _ in range(int(input()))], key=lambda x: x[0]**2+x[1]**2))