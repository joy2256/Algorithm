# 네트워크
#bfs -> 깊이가 중요할 때
#dfs -> 끝까지 탐색해야 할 때
#bfs
from collections import deque
def solution1(n, computers):
    def bfs(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for j in range(n):
                if computers[i][j] and not visited[j]:
                    q.append(j)

    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer

    #dfs
def solution2(n, computers):
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] and not visited[j]:
                dfs(j)
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
