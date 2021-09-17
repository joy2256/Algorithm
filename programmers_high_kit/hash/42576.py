# 완주하지 못한 선수

# 효율성 통과 X
def solution1(participant, completion):
    for p in completion:
        if p in participant:
            participant.remove(p)
    answer = participant[0]
    return answer

# hash 이용
# key를 해시값으로, 다 더해서 completion에 있는값들 빼줌
def solution2(participant, completion):
    d = dict()
    hashValue = 0
    for p in participant:
        d[hash(p)] = p
        hashValue += hash(p)
    for c in completion:
        hashValue -= hash(c)
    return d[hashValue]

# counter를 이용
import collections
def solution3(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution3(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))