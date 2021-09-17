from collections import deque
def solution_queue(prices):
    queue = deque(prices)
    answer = []
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer

def solution_stack(prices):
    length = len(prices)
    answer = [ i for i in range(length-1, -1, -1 )] #최적상태로 초기화
    stack = [0]
    for i in range(1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
print(solution_stack([1,2,3,2,3]))