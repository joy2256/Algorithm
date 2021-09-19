# 모의고사

def solution(answers):
    score = [0] * 4
    length = len(answers)
    student1 = [1, 2, 3, 4, 5] * (length // 5 + 1)
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * (length // 8 + 1)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (length // 10 + 1)
    for i in range(len(answers)):
        if answers[i] == student1[i]:
            score[1] += 1
        if answers[i] == student2[i]:
            score[2] += 1
        if answers[i] == student3[i]:
            score[3] += 1
    answer = list(filter(lambda i : score[i] == max(score), range(len(score))))
    
    return answer

print(solution([1, 3, 2, 4, 2]))