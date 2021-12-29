# 마법사 상어와 토네이도
# 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6 

n = int(input())
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)
start = n // 2 + 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = start, start
for i in range(1, n):
    for j in range(i):
        x += dx[0]
        
