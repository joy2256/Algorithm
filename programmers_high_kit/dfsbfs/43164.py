# 여행경로
#dfs 
def solution(tickets):
    answer = []
    stacks = ["ICN"]
    visited = [0 for i in range(len(tickets))]
    while stacks:
        top = stacks.pop()
        for i in range(len(tickets)):
            if visited[i] != 0:
                continue
            if tickets[i][0] == top:
                visited[i] = 1
                stacks.append(tickets[i][1])
            
    return answer

# 인터넷 풀이
def solution(tickets):
    # 그래프 생성
    routes = dict()
    for start, end in tickets:
        routes[start] = routes.get(start, []) + [end]
    # 끝점 역순으로 정렬
    for r in routes.keys():
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    answer = path[::-1]
    return answer 