# 강을 가로지르는 하나의 차선으로 된 다리가 하나 있다. 이 다리를 n개의 트럭이 건너가려고 한다. 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다.
# 다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다. 다리의 길이는 w 단위길이이며, 각 트럭들은 하나의 단위시간에 하나의 단위길이만큼만 이동할 수 있다고 가정한다.
# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.
# 참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.
# 다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때, 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성하라.
# 입력: 입력 데이터는 표준입력을 사용한다. 입력은 두 줄로 이루어진다.
# 입력의 첫 번째 줄에는 세 개의 정수 n, w, L이 주어지는데, n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다.
# 입력의 두 번째 줄에는 n개의 정수 a1, a2, ..., an이 주어지는데, ai는 i번째 트럭의 무게를 나타낸다.
# 출력: 출력은 표준 출력을 사용한다. 모든 트럭들이 다리를 건너는 최단 시간을 출력하라.
import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())    # 트럭의 개수, 다리 길이, 다리의 최대 하중
a = deque(map(int, sys.stdin.readline().split()))    # 트럭의 무게들
bridge = deque(0 for i in range(w))    # 다리의 상태
time = 0   # 모든 트럭들이 다리를 건너는데 드는 시간

while a:
    time += 1
    bridge.popleft()
    if sum(bridge) + a[0] <= L:
        bridge.append(a.popleft())
    else:
        bridge.append(0)

while sum(bridge) > 0:
    time += 1
    bridge.popleft()
    bridge.append(0)
print(time)
