# 치킨 배달

# 최소거리 구하는 함수
# 조합 다 확인해보고 최솟값인거 구하기

from itertools import combinations
def find_min_chicken(pos, chicken_list):
    min_len = 1000000
    for chicken in chicken_list:
        tmp_len = abs(pos[0]-chicken[0]) + abs(pos[1]-chicken[1])
        min_len = min(min_len, tmp_len)
    return min_len

N, M = map(int, input().strip().split())
NN = []
chicken_list = []
house_list = []
min_value = 10000000
for i in range(N):
    L = list(map(int, input().strip().split()))
    NN.append(L)
for i in range(N):
    for j in range(N):
        if NN[i][j] == 2:
            chicken_list.append([i,j])
        elif NN[i][j] == 1:
            house_list.append([i, j])

#chicken list m 만큼 고르기
sel_chik_list = list(combinations(chicken_list, M))
#모든 집에 대해 find_min_chicken한 뒤 합 구하기
for sel_chik in sel_chik_list:
    tmp = 0
    for house in house_list:
        tmp += find_min_chicken(house, sel_chik)
    min_value = min(min_value, tmp)
#최소인거 찾기
print(min_value)