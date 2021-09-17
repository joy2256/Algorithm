# 더 맵게
import heapq
def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    answer = 0
    while heap[0] < K and len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first + second * 2)
        answer += 1
    if len(heap) == 1 and heap[0] < K:
        answer = -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))