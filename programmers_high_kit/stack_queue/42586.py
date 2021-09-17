from collections import deque
import math

def solution(progresses, speeds):
    deq = deque()
    for p, s in zip(progresses, speeds):
        deq.append(math.ceil((100 - p) / s))
    
    answer = []
    old = deq.popleft()
    ans = 1
    while deq:
        new = deq.popleft()
        if old >= new:
            ans += 1
        else:
            answer.append(ans)
            old = new
            ans = 1
    answer.append(ans)

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))