# Lv.2 | 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# bridge_length: 다리에 올라갈 수 있는 트럭 수 (= 다리의 길이)
# weight: 다리가 견딜 수 있는 최대 무게
# truck_weights: 트럭별 무게를 담은 리스트
# bridge: 다리의 상태를 나타내는 큐
# total_weights: 현재 다리 위에 있는 트럭 무게의 총합
from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    total_weights = 0

    while bridge:
        # 매 시간마다 다리 위에 있는 트럭을 한 칸씩 전진시키고, 다리를 나가는 트럭의 무게를 total_weights에서 뺌
        time += 1
        total_weights -= bridge.popleft()

        if truck_weights:
            # 다리가 견딜 수 있는 무게(weight)를 초과하지 않으면 다리에 트럭을 추가
            if total_weights + truck_weights[0] <= weight:
                total_weights += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:   # 트럭이 건널 수 없다면 0을 넣어줌
                bridge.append(0)

    return time

solution(2, 10, [7, 4, 5, 6])
