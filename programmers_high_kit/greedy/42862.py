#체육복
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n + 1):
        if i not in lost:
            answer += 1
        else:
            if i - 1 in reserve and i - 1 not in lost:
                reserve.remove(i - 1)
                answer += 1
            elif i in reserve:
                reserve.remove(i)
                answer += 1
            elif i + 1 in reserve and i + 1 not in lost:
                reserve.remove(i + 1)
                answer += 1
    return answer