# 이중우선순위큐
import heapq
def solution(operations):
    heap = []
    for op in operations:
        cur = op.split()
        if cur[0] == "I":
            heapq.heappush(heap, int(cur[1]))
        if cur[0] == "D":
            if heap:
                if int(cur[1]) == -1:
                    heapq.heappop(heap)
                elif int(cur[1]) == 1:
                    heap = heapq.nlargest(len(heap), heap)[1:]
                    heapq.heapify(heap)
    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.heappop(heap)]
    else:
        return [0, 0]

print(solution(["I 7","I 5","I -5","D -1"]))
