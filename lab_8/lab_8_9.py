
n,l=map(int, input().split())
matrix=[(input().split()+['0']*l)[:l] for _ in range(n)]
rev_matrix=[[matrix[j][i] for j in range(n)] for i in range(l)] 
 
for pos1 in range(n):
    pos2=matrix[pos1].index(max(matrix[pos1]))
    if (max(matrix[pos1]) == min(rev_matrix[pos2])):
        matrix[pos1][pos2]+='!'
 
for line in matrix: 
    print(*line)