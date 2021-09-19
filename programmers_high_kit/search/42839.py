# 소수 찾기
from itertools import permutations
import math
def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def solution(numbers):
    answer = 0
    num = list(numbers)
    permut = []
    for i in range(1, 8):
        tmp = list(map(''.join, permutations(num, i)))
        for n in tmp:
            permut.append(int(n))
    permut = list(set(permut))
    if 0 in permut:
        permut.remove(0)
    print(permut)
    for p in permut:
        if is_prime_num(p):
            answer += 1
    return answer
print(solution("011"))
