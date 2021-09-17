def solution(priorities, location):
    loc = [i for i in range(len(priorities))]
    final_loc = []
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            final_loc.append(loc.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
    return final_loc.index(location) + 1

def solution2(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): # any : 반복 가능한 자료형 중 하나라도 True일 경우 True를 return
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

#런타임에러 케이스 존재
def my_solution(priorities, location):
    q = priorities
    loc = location
    print = 0
    while loc != -1:
        temp = q.pop(0)
        loc -= 1
        if temp >= max(priorities):
            print += 1
        else:
            q.append(temp)
            if loc == -1:
                loc += len(priorities)
    return print



print(solution([1, 1, 9, 1, 1, 1], 0))

