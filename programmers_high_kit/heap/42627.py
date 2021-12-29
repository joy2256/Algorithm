# 디스크 컨트롤러
# start : 바로 이전에 완료한 작업의 시작 시간
# now : 현재 시점
# heap : [작업의 소요 시간, 작업이 요청되는 시점]
import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 # 이전에 완료한 작업의 시작 시간
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            # 현재 시점에서 완료 가능한 작업들을 힙에 넣는다
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            curr = heapq.heappop(heap)
            start = now # 해당 작업을 시작시켜줌
            now += curr[0] # 해당 작업이 끝남
            answer += (now - curr[1])
            i += 1
        else:
            #실행시킬 작업이 없으면 시간을 지나보냄
            now += 1
    
    return int(answer / len(jobs))