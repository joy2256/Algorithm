# 타겟 넘버
#bfs
from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1*numbers[0], 0])
    while q:
        temp, idx = q.popleft()
        idx += 1
        if idx < len(numbers):
            q.append([temp + numbers[idx], idx])
            q.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer