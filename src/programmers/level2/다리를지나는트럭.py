from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    bridge_weight = 0

    while truck_weights:
        time += 1
        bridge_weight -= bridge.popleft()
        if bridge_weight + truck_weights[0] > weight:
            bridge.append(0)
        elif truck_weights:
            bridge.append(truck_weights[0])
            bridge_weight += truck_weights[0]
            del truck_weights[0]
    return time+bridge_length


result = solution(2, 10, [7, 4, 5, 6])
print(result)
