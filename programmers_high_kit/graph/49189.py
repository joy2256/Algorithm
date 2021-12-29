# 가장 먼 노드
#dfs로 순회
from collections import deque

def solution(n, edge):
    #그래프 생성
    edge.sort()
    graph = dict()
    for e1, e2 in edge:
        graph[e1] = graph.get(e1, []) + [e2]     
        graph[e2] = graph.get(e2, []) + [e1]

    route = [-1] * (n+1)
    q = deque()
    q.append(1)
    route[1] = 0
    while q:
        idx = q.popleft()
        for i in graph[idx]:
            if route[i] == -1:
                q.append(i)
                route[i] = route[idx] + 1

    return route.count(max(route))