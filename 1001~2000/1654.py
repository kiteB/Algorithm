# 박성원은 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다. 이미 오영식은 자체적으로 K개의 랜선을 가지고 있다.
# 그러나 K개의 랜선의 길이는 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었끼 때문에 K개의 랜선을 잘라서 만들어야 한다.
# 편의를 위해 랜선을 자르거나 만들 떄 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
# 그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자르다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
# 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. 항상 K <= N이다.
# 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 정수로 입력된다.
# 출력: 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
import sys

K, N = map(int, sys.stdin.readline().split())
LAN = []

for i in range(K):
    LAN.append(int(sys.stdin.readline()))


def cutting(target, data):
    start = 1
    end = max(data)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for i in data:
            if i >= mid:
                total += (i // mid)

        if total < target:
            end = mid - 1

        else:
            result = mid
            start = mid + 1

    return result


print(cutting(N, LAN))