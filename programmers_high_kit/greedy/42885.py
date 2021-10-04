# 구명보트
# 정렬해서 앞, 뒤만 비교
from collections import deque
def solution(people, limit):
    answer = 0
    left = deque(sorted(people))
    while left:
        if len(left) >= 2:
            if left[0] + left[-1] <= limit:
                left.popleft()
                left.pop()
                answer += 1
            else:
                left.pop()
                answer += 1
        else:
            left.pop()
            answer += 1
    return answer
# 시간초과로 실패..!!, 최대 2명씩만 탈수 있다는걸 인지못함
def solution_fail(people, limit):
    answer = 0
    stack = []
    peoples = sorted(people)
    while people:
        if sum(stack) < limit:
            for people in peoples:
                if sum(stack) + people <= limit:
                    stack.append(people)
                    peoples.remove(people)
                else: 
                    break
        else:
            stack.clear()
            answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))

#인터넷참고
