# K번째 수
def solution(array, commands):
    answer = []
    for command in commands:
        #크기만큼 자르고 정렬
        tmp = sorted(array[command[0]-1:command[1]])
        answer.append(tmp[command[2] - 1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

#참고 -> for가 아닌 map 사용하기
def solution2(array, commands):
    return list(map(lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1], commands))