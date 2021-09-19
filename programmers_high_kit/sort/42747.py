# H-index
def solution(citations):
    answer = 0
    citations = sorted(citations)
    for i in range(len(citations)):
        if citations[i] <= len(citations) - i:
            answer = citations[i]
        else: 
            if len(citations)-i > answer:
                answer = len(citations)-i
    return answer

print(solution([3, 0, 6, 1, 5]))