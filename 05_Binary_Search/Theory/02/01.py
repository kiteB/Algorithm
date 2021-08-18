import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))


def cutting(target, data):
    start = 0
    end = max(data)

    while start <= end:
        mid = (start + end) // 2
        result = 0              # 잘린 떡의 합

        for i in data:
            if i > mid:
                result += i - mid

        # 떡볶이의 양이 부족한 경우
        if result < target:
            end = mid - 1
        # 떡볶이의 양이 충분한 경우
        else:
            answer = mid
            start = mid + 1

    return answer


print(cutting(m, data))
