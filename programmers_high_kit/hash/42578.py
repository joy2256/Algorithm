# 위장
import collections
def solution(clothes):
    d = collections.Counter(c[1] for c in clothes)
    answer = 1
    for val in d.values():
        answer = answer * (val + 1)
    return answer - 1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))