# 조합으로 경우의 수 구하기
# 최소값 찾기
import sys, copy

zone =[]
max_safe = 0
virus = []
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    zone.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    for j in range(M):
        if zone[i][j] == 2:
            virus.append([i, j]) #y, x
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def select_wall(start, count):
    global max_safe
    if count == 3:
        # 벽이 다 세워진 이후
        sel_zone = copy.deepcopy(zone)
        for num in range(len(virus)):
            y, x = virus[num]
            spread(y, x, sel_zone)
            safe_count = sum(i.count(0) for i in sel_zone)
            max_safe = max(max_safe, safe_count)
        return True
    else:
        # 벽 선택
        for i in range(start, N*M):
            y = i // M
            x = i % M
            if zone[y][x] == 0:
                zone[y][x] = 1
                select_wall(i, count + 1)
                zone[y][x] = 0 

def spread(y, x, sel_zone):
    if sel_zone[y][x] == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny >= 0 and ny < N and nx >= 0 and nx < M:
                if sel_zone[ny][nx] == 0:
                    sel_zone[ny][nx] = 2
                    spread(ny, nx, sel_zone)
    

select_wall(0, 0)
print(max_safe)


