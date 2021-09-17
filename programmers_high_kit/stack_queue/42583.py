def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    time = 0
    while queue:
        time += 1
        queue.pop(0)
        if truck_weights:
            #sum에서 시간이 느려짐.
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
    
    return time

def solution2(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    time = 0
    curr_weight = 0  #sum을 없애기 위해 비교 가능한 현재 무게값을 만듦
    while queue:
        time += 1
        curr_weight -= queue.pop(0)
        if truck_weights:
            if curr_weight + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
                curr_weight += queue[-1]
            else:
                queue.append(0)
    
    return time
print(solution2(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))