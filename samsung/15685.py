# 드래곤 커브
G = [[0 for i in range(100)] for j in range(100)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dragon_curve(count, end, curve):
    if count == 0:
        tmp = curve[0]
        tmp[0] + dx[tmp[2]], tmp[1] + dy[tmp[2]] 