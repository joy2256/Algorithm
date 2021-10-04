# 섬 연결하기 -> 크루스칼 알고리즘

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connect = set([costs[0][0]])

    while len(connect) != n:
        for cost in costs:
            # 같은 tree에 있는지 확인
            if cost[0] and cost[1] in connect:
                continue
            # 같은 tree에 없을 경우 연결시켜줌
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer