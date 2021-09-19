def solution(brown, yellow):
    possible = []
    for i in range(1, yellow + 1):
        # i는 yellow의 세로 길이, 가로는 yellow // i (나머지 0일때)
        if yellow // i < i:
            break
        if yellow % i == 0:
            possible.append([yellow // i, i])
    for p in possible:
        if brown == (2 * (p[0] + 2) + 2 * p[1]):
            answer = [p[0] + 2, p[1] + 2]

    return answer

print(solution(24, 24))