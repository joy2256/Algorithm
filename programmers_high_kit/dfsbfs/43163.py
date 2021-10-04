# 단어 변환 dfs 이용
def solution(begin, target, words):
    def check(word1, word2):
        answer = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                answer += 1
        return True if answer == 1 else False

    answer = 0
    stack = [begin]
    visited = [0 for i in range(len(words))]
    if target not in words:
        return answer
    while stack:
        top = stack.pop()
        if top == target:
            return answer
        for i, word in enumerate(words):
            if check(top, word):
                if visited[i] != 0:
                    continue
                visited[i] = 1
                stack.append(word)
        answer += 1

    return answer
