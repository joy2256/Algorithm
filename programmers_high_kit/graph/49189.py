# 가장 먼 노드
#dfs로 순회
from collections import deque

def solution(n, edge):
    #그래프 생성
    graph = dict()
    for e1, e2 in edge:
        graph[e1] = graph.get(e1, []) + [e2]     
        graph[e2] = graph.get(e2, []) + [e1]

    visited = [-1 for i in range(n+1)]
    q = deque() #[노드번호, 깊이]
    q.append([1, 0])
    while q:
        idx, depth = q.popleft()
        visited[idx] = depth
        for i in graph[idx]:
            if visited[i] == -1:
                visited[i] == 0
                q.append([i, depth+1])
        depth += 1
    return visited.count(max(visited))